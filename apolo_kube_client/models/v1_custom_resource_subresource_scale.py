from pydantic import BaseModel, Field


class V1CustomResourceSubresourceScale(BaseModel):
    label_selector_path: str | None = Field(None, alias="labelSelectorPath")

    spec_replicas_path: str | None = Field(None, alias="specReplicasPath")

    status_replicas_path: str | None = Field(None, alias="statusReplicasPath")
