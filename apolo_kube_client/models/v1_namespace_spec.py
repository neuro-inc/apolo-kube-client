from pydantic import BaseModel, Field


class V1NamespaceSpec(BaseModel):
    finalizers: list[str] | None = Field(None, alias="finalizers")
