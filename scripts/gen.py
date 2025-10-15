import re
import string
from pathlib import Path

from kubernetes.client import models

from apolo_kube_client import models as apolo_models

MOD = """
from pydantic import BaseModel, Field
{imports}

class {clsname}(BaseModel):
{body}
"""

LIST_RE = re.compile(r"^list\[(?P<subtype>.+)\]$")
DICT_RE = re.compile(r"^dict\((?P<keytype>.+), (?P<valtype>.+)\)$")

TRANS = str.maketrans({ch: "_" + ch.lower() for ch in string.ascii_uppercase})


def mod_name(cls_name: str) -> str:
    return cls_name[0].lower() + cls_name[1:].translate(TRANS)


def parse_type(descr: str) -> set[str]:
    ret: set[str] = set()
    if match := DICT_RE.match(descr):
        ret |= parse_type(match.group("keytype"))
        ret |= parse_type(match.group("valtype"))
    elif match := LIST_RE.match(descr):
        ret |= parse_type(match.group("subtype"))
    else:
        if descr not in ("int", "bool", "int", "float", "str"):
            assert "[" not in descr, descr
            match descr:
                case "datetime":
                    ret.add("from datetime import datetime")
                case _:
                    ret.add(f"from .{mod_name(descr)} import {descr}")
    return ret


def generate(cls: type, target_dir: Path, init_lines: list[str]) -> None:
    _, _, modname = cls.__module__.rpartition(".")
    name = cls.__name__
    imports: set[str] = set()
    body: list[str] = []
    for attr, typ in cls.openapi_types.items():
        alias = cls.attribute_map[attr]
        field = f'{attr}: {typ} | None = Field(None, alias="{alias}")'
        imports |= parse_type(typ)
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
