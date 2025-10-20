from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1alpha1PodCertificateRequestSpec",)


class V1alpha1PodCertificateRequestSpec(BaseModel):
    max_expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="maxExpirationSeconds",
        validation_alias=AliasChoices("max_expiration_seconds", "maxExpirationSeconds"),
    )

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
    )

    node_uid: str | None = Field(
        default=None,
        serialization_alias="nodeUID",
        validation_alias=AliasChoices("node_uid", "nodeUID"),
    )

    pkix_public_key: str | None = Field(
        default=None,
        serialization_alias="pkixPublicKey",
        validation_alias=AliasChoices("pkix_public_key", "pkixPublicKey"),
    )

    pod_name: str | None = Field(
        default=None,
        serialization_alias="podName",
        validation_alias=AliasChoices("pod_name", "podName"),
    )

    pod_uid: str | None = Field(
        default=None,
        serialization_alias="podUID",
        validation_alias=AliasChoices("pod_uid", "podUID"),
    )

    proof_of_possession: str | None = Field(
        default=None,
        serialization_alias="proofOfPossession",
        validation_alias=AliasChoices("proof_of_possession", "proofOfPossession"),
    )

    service_account_name: str | None = Field(
        default=None,
        serialization_alias="serviceAccountName",
        validation_alias=AliasChoices("service_account_name", "serviceAccountName"),
    )

    service_account_uid: str | None = Field(
        default=None,
        serialization_alias="serviceAccountUID",
        validation_alias=AliasChoices("service_account_uid", "serviceAccountUID"),
    )

    signer_name: str | None = Field(
        default=None,
        serialization_alias="signerName",
        validation_alias=AliasChoices("signer_name", "signerName"),
    )
