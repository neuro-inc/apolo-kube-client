from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ListModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_list_meta import V1ListMeta
from .v1_validating_admission_policy_binding import V1ValidatingAdmissionPolicyBinding
from pydantic import BeforeValidator

__all__ = ("V1ValidatingAdmissionPolicyBindingList",)


class V1ValidatingAdmissionPolicyBindingList(ListModel):
    """ValidatingAdmissionPolicyBindingList is a list of ValidatingAdmissionPolicyBinding."""

    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicyBindingList"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="admissionregistration.k8s.io",
        kind="ValidatingAdmissionPolicyBindingList",
        version="v1",
    )

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    items: Annotated[
        list[V1ValidatingAdmissionPolicyBinding],
        Field(description="""List of PolicyBinding."""),
    ]

    kind: Annotated[
        str | None,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    metadata: Annotated[
        V1ListMeta,
        Field(
            description="""Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds""",
            exclude_if=lambda v: v == V1ListMeta(),
        ),
        BeforeValidator(_default_if_none(V1ListMeta)),
    ] = V1ListMeta()
