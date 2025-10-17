from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1IPBlock",)


class V1IPBlock(BaseModel):
    cidr: str | None = Field(default=None)

    except_: list[str] = Field(
        default=[],
        serialization_alias="except",
        validation_alias=AliasChoices("except_", "except"),
    )
