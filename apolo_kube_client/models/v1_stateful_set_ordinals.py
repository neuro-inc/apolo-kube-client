from pydantic import BaseModel, Field


class V1StatefulSetOrdinals(BaseModel):
    start: int | None = Field(None, alias="start")
