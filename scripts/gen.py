import keyword
import re
from pathlib import Path

from kubernetes.client import models
from pydantic import BaseModel

from apolo_kube_client import models as apolo_models

MOD = """
from __future__ import annotations
from pydantic import BaseModel, Field
{imports}

__all__ = ("{clsname}",)

class {clsname}(BaseModel):
{body}
"""

LIST_RE = re.compile(r"^list\[(?P<itemtype>.+)\]$")
DICT_RE = re.compile(r"^dict\((?P<keytype>.+), (?P<valtype>.+)\)$")


def mod_name(cls_name: str) -> str:
    obj = getattr(models, cls_name)
    _, _, mod_name = obj.__module__.rpartition(".")
    return mod_name


def parse_type(self_name: str, descr: str, imports: set[str]) -> str:
    descr = descr.strip()
    if descr == self_name:
        return descr
    elif descr == "object":
        imports.add("from apolo_kube_client._typedefs import JsonType")
        return "JsonType"
    elif match := DICT_RE.match(descr):
        keytype = parse_type(self_name, match.group("keytype"), imports)
        valtype = parse_type(self_name, match.group("valtype"), imports)
        return f"dict[{keytype}, {valtype}]"
    elif match := LIST_RE.match(descr):
        itemtype = parse_type(self_name, match.group("itemtype"), imports)
        return f"list[{itemtype}]"
    else:
        if descr not in ("int", "bool", "int", "float", "str"):
            assert "[" not in descr, descr
            assert not descr.startswith(("list", "dict")), descr
            match descr:
                case "datetime":
                    imports.add("from datetime import datetime")
                case _:
                    imports.add(f"from .{mod_name(descr)} import {descr}")
        return descr


def calc_attr_name(attr: str) -> str:
    if attr in dir(BaseModel) or keyword.iskeyword(attr):
        return "_" + attr
    else:
        return attr


def generate(cls: type, target_dir: Path, init_lines: list[str]) -> None:
    _, _, modname = cls.__module__.rpartition(".")
    name = cls.__name__
    imports: set[str] = set()
    body: list[str] = []
    for attr, typ in cls.openapi_types.items():
        alias = cls.attribute_map[attr]
        res_type = parse_type(name, typ, imports)
        real_attr = calc_attr_name(attr)
        field = f'{real_attr}: {res_type} | None = Field(None, alias="{alias}")'
        body.append(f"    {field}\n")
    mod = MOD.format(
        imports="\n".join(sorted(imports)), clsname=name, body="\n".join(body)
    )
    (target_dir / modname).with_suffix(".py").write_text(mod)
    init_lines.append(f"from .{modname} import {name} as {name}")


def main() -> None:
    target_dir = Path(apolo_models.__path__[0])
    init_lines: list[str] = []
    for name in dir(models):
        obj = getattr(models, name)
        if isinstance(obj, type):
            print(f"Generate {name}")
            generate(obj, target_dir, init_lines)

    (target_dir / "__init__.py").write_text("\n".join(init_lines))


if __name__ == "__main__":
    main()
