from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_validating_admission_policy_spec import V1ValidatingAdmissionPolicySpec
from .v1_validating_admission_policy_status import V1ValidatingAdmissionPolicyStatus
from pydantic import BeforeValidator

__all__ = ("V1ValidatingAdmissionPolicy",)


class V1ValidatingAdmissionPolicy(ResourceModel):
    """ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or rejects an object without changing it."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicy"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="admissionregistration.k8s.io",
        kind="ValidatingAdmissionPolicy",
        version="v1",
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "admissionregistration.k8s.io/v1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "ValidatingAdmissionPolicy"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1ValidatingAdmissionPolicySpec,
        Field(
            description="""Specification of the desired behavior of the ValidatingAdmissionPolicy.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ValidatingAdmissionPolicySpec)),
    ] = V1ValidatingAdmissionPolicySpec()

    status: Annotated[
        V1ValidatingAdmissionPolicyStatus,
        Field(
            description="""The status of the ValidatingAdmissionPolicy, including warnings that are useful to determine if the policy behaves in the expected way. Populated by the system. Read-only.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ValidatingAdmissionPolicyStatus)),
    ] = V1ValidatingAdmissionPolicyStatus()
