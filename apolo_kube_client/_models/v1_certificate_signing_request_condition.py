from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1CertificateSigningRequestCondition",)


class V1CertificateSigningRequestCondition(BaseModel):
    """CertificateSigningRequestCondition describes a condition of a CertificateSigningRequest object"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.certificates.v1.CertificateSigningRequestCondition"
    )

    last_transition_time: Annotated[
        datetime | None,
        Field(
            alias="lastTransitionTime",
            description="""lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition's status is changed, the server defaults this to the current time.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    last_update_time: Annotated[
        datetime | None,
        Field(
            alias="lastUpdateTime",
            description="""lastUpdateTime is the time of the last update to this condition""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""message contains a human readable message with details about the request state""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""reason indicates a brief reason for the request state""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        str,
        Field(
            description="""status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be "False" or "Unknown"."""
        ),
    ]

    type: Annotated[
        str,
        Field(
            description="""type of the condition. Known conditions are "Approved", "Denied", and "Failed".

An "Approved" condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.

A "Denied" condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.

A "Failed" condition is added via the /status subresource, indicating the signer failed to issue the certificate.

Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.

Only one condition of a given type is allowed."""
        ),
    ]
