from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1CustomResourceSubresourceScale",)


class V1CustomResourceSubresourceScale(BaseModel):
    label_selector_path: str | None = Field(None, alias="labelSelectorPath")

    spec_replicas_path: str | None = Field(None, alias="specReplicasPath")

    status_replicas_path: str | None = Field(None, alias="statusReplicasPath")
