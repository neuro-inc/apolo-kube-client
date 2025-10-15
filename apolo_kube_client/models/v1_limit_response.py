from pydantic import BaseModel, Field

from .v1_queuing_configuration import V1QueuingConfiguration


class V1LimitResponse(BaseModel):
    queuing: V1QueuingConfiguration | None = Field(None, alias="queuing")

    type: str | None = Field(None, alias="type")
