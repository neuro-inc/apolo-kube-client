from pydantic import BaseModel


__all__ = ("V1TopologySelectorLabelRequirement",)


class V1TopologySelectorLabelRequirement(BaseModel):
    key: str | None = None

    values: list[str] = []
