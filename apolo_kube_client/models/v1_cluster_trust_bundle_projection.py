from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector

__all__ = ("V1ClusterTrustBundleProjection",)


class V1ClusterTrustBundleProjection(BaseModel):
    label_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="labelSelector"
    )

    name: str | None = Field(default_factory=lambda: None)

    optional: bool | None = Field(default_factory=lambda: None)

    path: str | None = Field(default_factory=lambda: None)

    signer_name: str | None = Field(default_factory=lambda: None, alias="signerName")
