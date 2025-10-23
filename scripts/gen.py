import json
import keyword
import re
from dataclasses import dataclass
from pathlib import Path
from operator import itemgetter
import libcst
from kubernetes.client import models
from pydantic import BaseModel
from typing import Any
from copy import replace


MOD = """\
from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
{imports}

__all__ = ("{clsname}",)

class {clsname}({base}):
    '''{doc}'''

    model_config = ConfigDict(extra="forbid", validate_by_alias=True, validate_by_name=True)

    kubernetes_ref: ClassVar[Final[str]] = "{ref}"

{body}
"""

BASE_MOD = """\
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_list_meta import V1ListMeta


class ResourceModel(BaseModel):
    metadata: V1ObjectMeta = V1ObjectMeta()


class ListModel(BaseModel):
    metadata: V1ListMeta = V1ListMeta()
"""

UTILS_MOD = """\
from dataclasses import dataclass
from typing import Any, Callable
from pydantic import BaseModel


@dataclass(frozen=True)
class KubeMeta:
    group: str
    kind: str
    version: str


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


def _exclude_if(v: Any) -> bool:
    if v is None:
        return True
    if isinstance(v, BaseModel):
        type_ = type(v)
        required = any(f.is_required() for f in type_.model_fields.values())
        if required:
            return False
        return v.model_dump() == type_().model_dump()
    if isinstance(v, (list, dict)):
        return not v
    return False
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
    default: str | None
    is_model: bool
    is_collection: bool
    self_ref: bool = False


def parse_type(self_name: str, descr: str) -> ParseTypeRes:
    descr = descr.strip()
    if descr == self_name:
        return ParseTypeRes(
            f'"{descr} | None"',
            frozenset(),
            "None",  # avoid recursive ctor
            True,
            False,
            True,
        )
    elif descr == "object":
        return ParseTypeRes(
            "JsonType",
            frozenset(["from apolo_kube_client._typedefs import JsonType"]),
            "{}",
            False,
            False,
        )
    elif match := DICT_RE.match(descr):
        key = parse_type(self_name, match.group("key"))
        val = parse_type(self_name, match.group("val"))
        return ParseTypeRes(
            f"dict[{key.type_}, {val.type_}]",
            key.imports | val.imports,
            "{}",
            False,
            True,
        )
    elif match := LIST_RE.match(descr):
        item = parse_type(self_name, match.group("item"))
        return ParseTypeRes(
            f"list[{item.type_}]",
            item.imports,
            "[]",
            False,
            True,
        )
    else:
        match descr:
            case "int":
                return ParseTypeRes(
                    "int",
                    frozenset(),
                    "None",
                    False,
                    False,
                )
            case "bool":
                return ParseTypeRes(
                    "bool",
                    frozenset(),
                    "None",
                    False,
                    False,
                )
            case "int":
                return ParseTypeRes(
                    "int",
                    frozenset(),
                    "None",
                    False,
                    False,
                )
            case "float":
                return ParseTypeRes(
                    "float",
                    frozenset(),
                    "None",
                    False,
                    False,
                )
            case "str":
                return ParseTypeRes(
                    "str",
                    frozenset(),
                    "None",
                    False,
                    False,
                )
            case "datetime":
                return ParseTypeRes(
                    "datetime",
                    frozenset(["from datetime import datetime"]),
                    "None",
                    False,
                    False,
                )
            case _:
                return ParseTypeRes(
                    descr,
                    frozenset([f"from .{mod_name(descr)} import {descr}"]),
                    f"{descr}()",
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


def find_def(swagger: Any, name: str) -> tuple[str, Any]:
    prefixes = ("V1", "V1alpha1", "V1alpha2", "V1alpha3", "V1beta1", "V1beta2", "V2")
    found = []
    if name == "VersionInfo":
        tail = "version.Info"
    else:
        for prefix in reversed(prefixes):
            parts = name.split(prefix)
            if len(parts) == 1:
                continue
            assert len(parts) == 2, parts
            assert parts[-1] != ""
            if parts[0] != "":
                tail = f"{parts[0].lower()}.{prefix.lower()}.{parts[1]}"
            else:
                tail = f"{prefix.lower()}.{parts[1]}"
            break
        else:
            tail = name
    for ref in swagger["definitions"]:
        if ref == tail or ref.endswith("." + tail):
            found.append(ref)

    if not found:
        raise Exception(f"Cannot find definition for {name}")
    elif len(found) > 1:
        raise Exception(f"Found multiple definitions for {name}: {found}")

    return found[0], swagger["definitions"][found[0]]


def generate(
    cls: type,
    swagger: Any,
    target_dir: Path,
    visited: dict[str, bool],
    init_lines: list[str],
    all_names: list[str],
) -> None:
    _, _, modname = cls.__module__.rpartition(".")
    name = cls.__name__
    if name in visited:
        return
    print(f"Generate {name}")
    imports: set[str] = set()
    body: list[str] = []
    ref, definition = find_def(swagger, name)

    if "x-kubernetes-group-version-kind" in definition:
        meta: list[str] = []
        for group_version_kind in sorted(
            definition["x-kubernetes-group-version-kind"], key=itemgetter("group")
        ):
            meta.append(
                f'KubeMeta(group="{group_version_kind["group"]}", kind="{group_version_kind["kind"]}", version="{group_version_kind["version"]}")'
            )

        meta_str = ", ".join(meta)
        body.append(
            f"    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = ({meta_str})\n"
        )
        imports.add("from .utils import KubeMeta")

    required: set[str] = set(definition.get("required", []))

    match cls.openapi_types.get("metadata"):
        case None:
            base = "BaseModel"
        case "V1ObjectMeta":
            base = "ResourceModel"
            imports.add("from .base import ResourceModel")
        case "V1ListMeta":
            base = "ListModel"
            imports.add("from .base import ListModel")
    has_required = False
    for attr, typ in cls.openapi_types.items():
        alias = cls.attribute_map[attr]
        is_required = alias in required
        has_required |= is_required
        res = parse_type(name, typ)
        imports |= res.imports
        real_attr = calc_attr_name(attr)
        field_args: dict[str, str] = {}
        if alias != real_attr:
            field_args["alias"] = f'"{alias}"'

        attr_def = definition["properties"][alias]

        attr_descr = attr_def.get("description")
        if attr_descr:
            quota = (
                '"""'
                if not attr_descr.startswith('"') and not attr_descr.endswith('"')
                else "'''"
            )
            field_args["description"] = quota + attr_descr + quota

        annotations = []

        if is_required:
            res = replace(res, default=None)
        else:
            # field_args["exclude_if"] = "_exclude_if"
            # imports.add("from .utils import _exclude_if")

            if res.is_model:
                imports.add("from pydantic import BeforeValidator")
                imports.add("from .utils import _default_if_none")
                annotations.append(f"BeforeValidator(_default_if_none({res.type_}))")
                if not res.self_ref:
                    if res.type_ not in visited:
                        generate(
                            getattr(models, res.type_),
                            swagger,
                            target_dir,
                            visited,
                            init_lines,
                            all_names,
                        )
                    if visited[res.type_]:
                        res = replace(
                            res,
                            default="None",
                            type_=res.type_ + " | None",
                        )
            elif res.is_collection:
                imports.add("from pydantic import BeforeValidator")
                imports.add("from .utils import _collection_if_none")
                annotations.append(
                    f'BeforeValidator(_collection_if_none("{res.default}"))'
                )
            else:
                if res.type_ != "JsonType":
                    res = replace(
                        res,
                        default="None",
                        type_=res.type_ + " | None",
                    )
            field_args["exclude_if"] = (
                f"lambda v: v=={res.default}"
                if res.default != "None"
                else "lambda v: v is None"
            )

        field_str = ", ".join(f"{k}={v}" for k, v in field_args.items())
        annotations.insert(0, f"Field({field_str})")

        annotations_str = ", ".join(annotations)
        field = f"{real_attr}: Annotated[{res.type_}, {annotations_str}]"
        if res.default is not None:
            field += f" = {res.default}"

        body.append(f"    {field}\n")

    if "description" in definition:
        doc = definition["description"]
    else:
        doc = ""
    mod = MOD.format(
        imports="\n".join(sorted(imports)),
        clsname=name,
        base=base,
        doc=doc,
        ref=ref,
        body="\n".join(body),
    )
    (target_dir / modname).with_suffix(".py").write_text(mod)
    init_lines.append(f"from .{modname} import {name}")
    all_names.append(name)
    visited[name] = has_required


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
    with (here.parent / "swagger.json").open() as swagger_file:
        swagger = json.load(swagger_file)
    visited: dict[str, bool] = {}
    for name in dir(models):
        obj = getattr(models, name)
        if isinstance(obj, type):
            generate(obj, swagger, target_dir, visited, init_lines, all_names)

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
