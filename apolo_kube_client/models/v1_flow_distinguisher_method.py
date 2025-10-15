from pydantic import BaseModel, Field


class V1FlowDistinguisherMethod(BaseModel):
    type: str | None = Field(None, alias="type")
