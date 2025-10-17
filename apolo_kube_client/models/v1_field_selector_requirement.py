from pydantic import BaseModel


__all__ = ("V1FieldSelectorRequirement",)


class V1FieldSelectorRequirement(BaseModel):
    key: str | None = None

    operator: str | None = None

    values: list[str] = []
