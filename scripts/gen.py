import keyword
import re
from dataclasses import dataclass
from pathlib import Path

from kubernetes.client import models
from pydantic import BaseModel

MOD = """
from __future__ import annotations
from pydantic import BaseModel, Field
{imports}

__all__ = ("{clsname}",)

class {clsname}(BaseModel):
{body}
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


def parse_type(self_name: str, descr: str, *, nested: bool = False) -> ParseTypeRes:
    descr = descr.strip()
    if descr == self_name:
        return ParseTypeRes(descr, frozenset(), f"{descr}()")
    elif descr == "object":
        return ParseTypeRes(
            "JsonType",
            frozenset(["from apolo_kube_client._typedefs import JsonType"]),
            "{}",
        )
    elif match := DICT_RE.match(descr):
        key = parse_type(self_name, match.group("key"), nested=True)
        val = parse_type(self_name, match.group("val"), nested=True)
        return ParseTypeRes(
            f"dict[{key.type_}, {val.type_}]", key.imports | val.imports, "{}"
        )
    elif match := LIST_RE.match(descr):
        item = parse_type(self_name, match.group("item"), nested=True)
        return ParseTypeRes(f"list[{item.type_}]", item.imports, "[]")
    else:
        suffix = " | None" if not nested else ""
        match descr:
            case "int":
                return ParseTypeRes("int" + suffix, frozenset(), "None")
            case "bool":
                return ParseTypeRes("bool" + suffix, frozenset(), "None")
            case "int":
                return ParseTypeRes("int" + suffix, frozenset(), "None")
            case "float":
                return ParseTypeRes("float" + suffix, frozenset(), "None")
            case "str":
                return ParseTypeRes("str" + suffix, frozenset(), "None")
            case "datetime":
                return ParseTypeRes(
                    "datetime" + suffix,
                    frozenset(["from datetime import datetime"]),
                    "None",
                )
            case _:
                return ParseTypeRes(
                    descr,
                    frozenset([f"from .{mod_name(descr)} import {descr}"]),
                    f"{descr}()",
                )


def calc_attr_name(attr: str) -> str:
    if attr in dir(BaseModel) or keyword.iskeyword(attr):
        return attr + "_"
    elif attr.startswith("_") and keyword.iskeyword(attr[1:]):
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
    for attr, typ in cls.openapi_types.items():
        alias = cls.attribute_map[attr]
        res = parse_type(name, typ)
        imports |= res.imports
        real_attr = calc_attr_name(attr)
        field = f'{real_attr}: {res.type_} = Field(default_factory=lambda: {res.default}, alias="{alias}")'
        body.append(f"    {field}\n")
    mod = MOD.format(
        imports="\n".join(sorted(imports)), clsname=name, body="\n".join(body)
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

    all = ", ".join(f'"{name}"' for name in sorted(all_names))
    init_lines.append(f"__all__ = ({all})")
    (target_dir / "__init__.py").write_text("\n".join(init_lines))


if __name__ == "__main__":
    main()
