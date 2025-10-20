from pydantic import BaseModel


__all__ = ("V1ExternalDocumentation",)


class V1ExternalDocumentation(BaseModel):
    description: str | None = None

    url: str | None = None
