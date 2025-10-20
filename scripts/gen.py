import keyword
import re
from dataclasses import dataclass
from pathlib import Path

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


REQUIRED = {"V1ObjectMeta": {"name"}}
REQUIRED_ALL = {"metadata"}

REQUIRED = {}
REQUIRED_ALL = set()


def parse_type(self_name: str, descr: str, *, nested: bool = False) -> ParseTypeRes:
    descr = descr.strip()
    if descr == self_name:
        return ParseTypeRes(
            f'"{descr}"', frozenset(), f"default_factory=lambda: {descr}()"
        )
    elif descr == "object":
        return ParseTypeRes(
            "JsonType",
            frozenset(["from apolo_kube_client._typedefs import JsonType"]),
            "default={}",
        )
    elif match := DICT_RE.match(descr):
        key = parse_type(self_name, match.group("key"), nested=True)
        val = parse_type(self_name, match.group("val"), nested=True)
        return ParseTypeRes(
            f"dict[{key.type_}, {val.type_}]", key.imports | val.imports, "default={}"
        )
    elif match := LIST_RE.match(descr):
        item = parse_type(self_name, match.group("item"), nested=True)
        return ParseTypeRes(f"list[{item.type_}]", item.imports, "default=[]")
    else:
        suffix = " | None" if not nested else ""
        match descr:
            case "int":
                return ParseTypeRes("int" + suffix, frozenset(), "default=None")
            case "bool":
                return ParseTypeRes("bool" + suffix, frozenset(), "default=None")
            case "int":
                return ParseTypeRes("int" + suffix, frozenset(), "default=None")
            case "float":
                return ParseTypeRes("float" + suffix, frozenset(), "default=None")
            case "str":
                return ParseTypeRes("str" + suffix, frozenset(), "default=None")
            case "datetime":
                return ParseTypeRes(
                    "datetime" + suffix,
                    frozenset(["from datetime import datetime"]),
                    "default=None",
                )
            case _:
                return ParseTypeRes(
                    descr,
                    frozenset([f"from .{mod_name(descr)} import {descr}"]),
                    f"default_factory=lambda: {descr}()",
                )


TYPES = {"bool", "int", "float", "str"}


def calc_attr_name(attr: str) -> str:
    if attr in dir(BaseModel) or keyword.iskeyword(attr):
        return attr + "_"
    elif attr in TYPES:
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
        if attr in REQUIRED_ALL or attr in REQUIRED.get(name, set()):
            if real_alias:
                tail = f" = Field(...{real_alias})"
            else:
                tail = ""
            field = f"{real_attr}: {res.type_.removesuffix(' | None')}{tail}"
        else:
            if real_alias or "lambda" in res.default:
                tail = f" = Field({res.default}{real_alias})"
            else:
                tail = f" = {res.default.removeprefix('default=')}"
            field = f"{real_attr}: {res.type_}{tail}"
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


def main() -> None:
    here = Path(__file__)
    target_dir = here.parent.parent / "apolo_kube_client" / "models"
    init_lines: list[str] = []
    all_names: list[str] = []
    for name in dir(models):
        obj = getattr(models, name)
        if isinstance(obj, type):
            print(f"Generate {name}")
            generate(obj, target_dir, init_lines, all_names)

    (target_dir / "base.py").write_text(BASE_MOD)
    init_lines.append("from .base import ListModel, ResourceModel")
    all_names.extend(["ListModel", "ResourceModel"])

    all = ", ".join(f'"{name}"' for name in sorted(all_names))
    init_lines.append(f"__all__ = ({all})")
    (target_dir / "__init__.py").write_text("\n".join(init_lines))


if __name__ == "__main__":
    main()
