from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1IPBlock",)


class V1IPBlock(BaseModel):
    cidr: str | None = None

    except_: list[str] = Field(
        default=[],
        serialization_alias="except",
        validation_alias=AliasChoices("except_", "except"),
    )
