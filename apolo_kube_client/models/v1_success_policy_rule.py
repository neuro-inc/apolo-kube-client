from pydantic import BaseModel, Field


class V1SuccessPolicyRule(BaseModel):
    succeeded_count: int | None = Field(None, alias="succeededCount")

    succeeded_indexes: str | None = Field(None, alias="succeededIndexes")
