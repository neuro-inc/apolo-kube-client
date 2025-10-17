from pydantic import BaseModel


__all__ = ("V1LabelSelectorRequirement",)


class V1LabelSelectorRequirement(BaseModel):
    key: str | None = None

    operator: str | None = None

    values: list[str] = []
