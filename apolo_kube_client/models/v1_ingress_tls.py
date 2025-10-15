from pydantic import BaseModel, Field


class V1IngressTLS(BaseModel):
    hosts: list[str] | None = Field(None, alias="hosts")

    secret_name: str | None = Field(None, alias="secretName")
