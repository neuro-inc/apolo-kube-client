from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1alpha1PodCertificateRequestSpec",)


class V1alpha1PodCertificateRequestSpec(BaseModel):
    max_expiration_seconds: int | None = Field(
        default_factory=lambda: None, alias="maxExpirationSeconds"
    )

    node_name: str | None = Field(default_factory=lambda: None, alias="nodeName")

    node_uid: str | None = Field(default_factory=lambda: None, alias="nodeUID")

    pkix_public_key: str | None = Field(
        default_factory=lambda: None, alias="pkixPublicKey"
    )

    pod_name: str | None = Field(default_factory=lambda: None, alias="podName")

    pod_uid: str | None = Field(default_factory=lambda: None, alias="podUID")

    proof_of_possession: str | None = Field(
        default_factory=lambda: None, alias="proofOfPossession"
    )

    service_account_name: str | None = Field(
        default_factory=lambda: None, alias="serviceAccountName"
    )

    service_account_uid: str | None = Field(
        default_factory=lambda: None, alias="serviceAccountUID"
    )

    signer_name: str | None = Field(default_factory=lambda: None, alias="signerName")
