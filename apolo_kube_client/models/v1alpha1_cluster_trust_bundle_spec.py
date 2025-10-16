from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1alpha1ClusterTrustBundleSpec",)


class V1alpha1ClusterTrustBundleSpec(BaseModel):
    signer_name: str | None = Field(default_factory=lambda: None, alias="signerName")

    trust_bundle: str | None = Field(default_factory=lambda: None, alias="trustBundle")
