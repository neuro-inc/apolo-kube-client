from pydantic import BaseModel, Field


class V1PersistentVolumeClaimVolumeSource(BaseModel):
    claim_name: str | None = Field(None, alias="claimName")

    read_only: bool | None = Field(None, alias="readOnly")
