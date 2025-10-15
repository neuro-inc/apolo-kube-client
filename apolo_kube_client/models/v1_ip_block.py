from pydantic import BaseModel, Field


class V1IPBlock(BaseModel):
    cidr: str | None = Field(None, alias="cidr")

    _except: list[str] | None = Field(None, alias="except")
