import keyword
import re
from dataclasses import dataclass
from pathlib import Path
import libcst

from kubernetes.client import models
from pydantic import BaseModel

MOD = """\
from pydantic import AliasChoices, BaseModel, Field
{imports}

__all__ = ("{clsname}",)

class {clsname}({base}):
{body}
"""

BASE_MOD = """\
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_list_meta import V1ListMeta


class ResourceModel(BaseModel):
    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())


class ListModel(BaseModel):
    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
"""

UTILS_MOD = """\
from typing import Any, Callable

def _default_if_none[T](type_: type[T]) -> Callable[[Any], Any]:
    def validator(arg: Any) -> Any:
        if arg is None:
            return type_()
        else:
            return arg

    return validator


def _collection_if_none(type_: str) -> Callable[[Any], Any]:
    def validator(arg: Any) -> Any:
        if arg is None:
            return eval(type_)
        else:
            return arg

    return validator
"""


LIST_RE = re.compile(r"^list\[(?P<item>.+)\]$")
DICT_RE = re.compile(r"^dict\((?P<key>.+), (?P<val>.+)\)$")


def mod_name(cls_name: str) -> str:
    obj = getattr(models, cls_name)
    _, _, mod_name = obj.__module__.rpartition(".")
    return mod_name


@dataclass(frozen=True)
class ParseTypeRes:
    type_: str
    imports: frozenset[str]
    default: str
    is_model: bool
    is_collection: bool


def parse_type(self_name: str, descr: str, *, nested: bool = False) -> ParseTypeRes:
    descr = descr.strip()
    if descr == self_name:
        if not nested:
            return ParseTypeRes(
                f'"{descr} | None"',
                frozenset(),
                "default=None",  # avoid recursive ctor
                True,
                False,
            )
        else:
            return ParseTypeRes(
                f'"{descr}"',
                frozenset(),
                f"default_factory=lambda: {descr}()",
                True,
                False,
            )
    elif descr == "object":
        return ParseTypeRes(
            "JsonType",
            frozenset(["from apolo_kube_client._typedefs import JsonType"]),
            "default={}",
            False,
            False,
        )
    elif match := DICT_RE.match(descr):
        key = parse_type(self_name, match.group("key"), nested=True)
        val = parse_type(self_name, match.group("val"), nested=True)
        return ParseTypeRes(
            f"dict[{key.type_}, {val.type_}]",
            key.imports | val.imports,
            "default={}",
            False,
            True,
        )
    elif match := LIST_RE.match(descr):
        item = parse_type(self_name, match.group("item"), nested=True)
        return ParseTypeRes(
            f"list[{item.type_}]", item.imports, "default=[]", False, True
        )
    else:
        suffix = " | None" if not nested else ""
        match descr:
            case "int":
                return ParseTypeRes(
                    "int" + suffix, frozenset(), "default=None", False, False
                )
            case "bool":
                return ParseTypeRes(
                    "bool" + suffix, frozenset(), "default=None", False, False
                )
            case "int":
                return ParseTypeRes(
                    "int" + suffix, frozenset(), "default=None", False, False
                )
            case "float":
                return ParseTypeRes(
                    "float" + suffix, frozenset(), "default=None", False, False
                )
            case "str":
                return ParseTypeRes(
                    "str" + suffix, frozenset(), "default=None", False, False
                )
            case "datetime":
                return ParseTypeRes(
                    "datetime" + suffix,
                    frozenset(["from datetime import datetime"]),
                    "default=None",
                    False,
                    False,
                )
            case _:
                return ParseTypeRes(
                    descr,
                    frozenset([f"from .{mod_name(descr)} import {descr}"]),
                    f"default_factory=lambda: {descr}()",
                    True,
                    False,
                )


INVALID_NAMES = {"bool", "int", "float", "str"}


def calc_attr_name(attr: str) -> str:
    if attr in dir(BaseModel) or keyword.iskeyword(attr):
        return attr + "_"
    elif attr in INVALID_NAMES:
        return attr + "_"
    elif attr.startswith("_"):
        return attr[1:] + "_"
    else:
        return attr


def generate(
    cls: type, target_dir: Path, init_lines: list[str], all_names: list[str]
) -> None:
    _, _, modname = cls.__module__.rpartition(".")
    name = cls.__name__
    imports: set[str] = set()
    body: list[str] = []
    match cls.openapi_types.get("metadata"):
        case None:
            base = "BaseModel"
        case "V1ObjectMeta":
            base = "ResourceModel"
            imports.add("from .base import ResourceModel")
        case "V1ListMeta":
            base = "ListModel"
            imports.add("from .base import ListModel")
    for attr, typ in cls.openapi_types.items():
        alias = cls.attribute_map[attr]
        res = parse_type(name, typ)
        imports |= res.imports
        real_attr = calc_attr_name(attr)
        if alias != real_attr:
            choices = [real_attr, alias]
            choices_str = ", ".join(f'"{item}"' for item in choices)
            real_alias = (
                f', serialization_alias="{alias}", '
                f"validation_alias=AliasChoices({choices_str})"
            )
        else:
            real_alias = ""
        if real_alias or "lambda" in res.default:
            tail = f" = Field({res.default}{real_alias})"
        else:
            tail = f" = {res.default.removeprefix('default=')}"
        type_ = res.type_
        if res.is_model:
            imports.add("from typing import Annotated")
            imports.add("from pydantic import BeforeValidator")
            imports.add("from .utils import _default_if_none")
            type_ = f"Annotated[{type_}, BeforeValidator(_default_if_none({type_}))]"
        elif res.is_collection:
            imports.add("from typing import Annotated")
            imports.add("from pydantic import BeforeValidator")
            imports.add("from .utils import _collection_if_none")
            type_ = f'Annotated[{type_}, BeforeValidator(_collection_if_none("{res.default.removeprefix("default=")}"))]'
        field = f"{real_attr}: {type_}{tail}"
        body.append(f"    {field}\n")
    mod = MOD.format(
        imports="\n".join(sorted(imports)),
        clsname=name,
        base=base,
        body="\n".join(body),
    )
    (target_dir / modname).with_suffix(".py").write_text(mod)
    init_lines.append(f"from .{modname} import {name}")
    all_names.append(name)


class Transformer(libcst.CSTTransformer):
    def __init__(self, names: list[str]) -> None:
        self._names = sorted(names)

    def visit_ImportFrom(self, node: libcst.ImportFrom) -> bool | None:
        return False

    def leave_ImportFrom(
        self, original: libcst.ImportFrom, updated: libcst.ImportFrom
    ) -> libcst.ImportFrom:
        if updated.module.value == "_models":
            return updated.with_changes(
                names=[
                    libcst.ImportAlias(libcst.Name(value=name)) for name in self._names
                ]
            )
        return updated

    def visit_Assign(self, node: libcst.Assign) -> bool | None:
        return False

    def leave_Assign(
        self, original: libcst.Assign, updated: libcst.Assign
    ) -> libcst.Assign:
        if updated.targets[0].target.value == "__all__":
            existing_all = [elem.value.value for elem in updated.value.elements]
            new_all = sorted(set(existing_all + [f'"{name}"' for name in self._names]))
            return updated.with_changes(
                value=libcst.List(
                    elements=[
                        libcst.Element(value=libcst.SimpleString(value=name))
                        for name in new_all
                    ],
                    lbracket=updated.value.lbracket,
                    rbracket=updated.value.rbracket,
                )
            )

        return updated


def fix_init(root_dir: Path, all_names: list[str]) -> None:
    fname = root_dir / "__init__.py"
    mod = libcst.parse_module(fname.read_text())
    updated_mod = mod.visit(Transformer(all_names))
    fname.write_text(updated_mod.code)


def main() -> None:
    here = Path(__file__)
    root_dir = here.parent.parent / "apolo_kube_client"
    target_dir = root_dir / "_models"
    target_dir.mkdir(exist_ok=True)
    init_lines: list[str] = []
    all_names: list[str] = []
    for name in dir(models):
        obj = getattr(models, name)
        if isinstance(obj, type):
            print(f"Generate {name}")
            generate(obj, target_dir, init_lines, all_names)

    (target_dir / "base.py").write_text(BASE_MOD)
    (target_dir / "utils.py").write_text(UTILS_MOD)
    init_lines.append("from .base import ListModel, ResourceModel")
    all_names.extend(["ListModel", "ResourceModel"])

    all = ", ".join(f'"{name}"' for name in sorted(all_names))
    init_lines.append(f"__all__ = ({all})")
    (target_dir / "__init__.py").write_text("\n".join(init_lines))

    fix_init(root_dir, all_names)


if __name__ == "__main__":
    main()
