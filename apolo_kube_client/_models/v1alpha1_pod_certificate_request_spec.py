from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1alpha1PodCertificateRequestSpec",)


class V1alpha1PodCertificateRequestSpec(BaseModel):
    max_expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="maxExpirationSeconds",
        validation_alias=AliasChoices("max_expiration_seconds", "maxExpirationSeconds"),
        exclude_if=_exclude_if,
    )

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
        exclude_if=_exclude_if,
    )

    node_uid: str | None = Field(
        default=None,
        serialization_alias="nodeUID",
        validation_alias=AliasChoices("node_uid", "nodeUID"),
        exclude_if=_exclude_if,
    )

    pkix_public_key: str | None = Field(
        default=None,
        serialization_alias="pkixPublicKey",
        validation_alias=AliasChoices("pkix_public_key", "pkixPublicKey"),
        exclude_if=_exclude_if,
    )

    pod_name: str | None = Field(
        default=None,
        serialization_alias="podName",
        validation_alias=AliasChoices("pod_name", "podName"),
        exclude_if=_exclude_if,
    )

    pod_uid: str | None = Field(
        default=None,
        serialization_alias="podUID",
        validation_alias=AliasChoices("pod_uid", "podUID"),
        exclude_if=_exclude_if,
    )

    proof_of_possession: str | None = Field(
        default=None,
        serialization_alias="proofOfPossession",
        validation_alias=AliasChoices("proof_of_possession", "proofOfPossession"),
        exclude_if=_exclude_if,
    )

    service_account_name: str | None = Field(
        default=None,
        serialization_alias="serviceAccountName",
        validation_alias=AliasChoices("service_account_name", "serviceAccountName"),
        exclude_if=_exclude_if,
    )

    service_account_uid: str | None = Field(
        default=None,
        serialization_alias="serviceAccountUID",
        validation_alias=AliasChoices("service_account_uid", "serviceAccountUID"),
        exclude_if=_exclude_if,
    )

    signer_name: str | None = Field(
        default=None,
        serialization_alias="signerName",
        validation_alias=AliasChoices("signer_name", "signerName"),
        exclude_if=_exclude_if,
    )
