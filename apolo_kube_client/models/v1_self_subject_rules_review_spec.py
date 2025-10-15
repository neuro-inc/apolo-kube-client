from pydantic import BaseModel, Field


class V1SelfSubjectRulesReviewSpec(BaseModel):
    namespace: str | None = Field(None, alias="namespace")
