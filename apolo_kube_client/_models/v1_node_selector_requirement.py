from pydantic import BaseModel


__all__ = ("V1NodeSelectorRequirement",)


class V1NodeSelectorRequirement(BaseModel):
    key: str | None = None

    operator: str | None = None

    values: list[str] = []
