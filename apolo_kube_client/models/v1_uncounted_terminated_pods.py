from pydantic import BaseModel, Field


class V1UncountedTerminatedPods(BaseModel):
    failed: list[str] | None = Field(None, alias="failed")

    succeeded: list[str] | None = Field(None, alias="succeeded")
