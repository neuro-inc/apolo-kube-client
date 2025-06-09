from typing import TypeAlias, TypeAliasType

PrimitiveType: TypeAlias = int | float | str | bool | None
JsonType = TypeAliasType(
    "JsonType", "PrimitiveType | list[JsonType] | dict[str, JsonType]"
)
