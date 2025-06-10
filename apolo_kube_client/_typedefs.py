from typing import TypeAlias, TypeAliasType

PrimitiveType: TypeAlias = int | float | str | bool | None
JsonType = TypeAliasType(
    "JsonType", "PrimitiveType | list[JsonType] | dict[str, JsonType]"
)

NestedStrKeyDict = TypeAliasType(
    "NestedStrKeyDict",
    "dict[str, PrimitiveType] | dict[str, NestedStrKeyDict] | dict[str, list[PrimitiveType | NestedStrKeyDict]]",
)
NestedStrKeyDictValue = TypeAliasType(
    "NestedStrKeyDictValue",
    "PrimitiveType | NestedStrKeyDict | list[PrimitiveType | NestedStrKeyDict]",
)
