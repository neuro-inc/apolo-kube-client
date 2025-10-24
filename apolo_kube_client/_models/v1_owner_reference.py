from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1OwnerReference",)


class V1OwnerReference(BaseModel):
    """OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.OwnerReference"
    )

    api_version: Annotated[
        str, Field(alias="apiVersion", description="""API version of the referent.""")
    ]

    block_owner_deletion: Annotated[
        bool | None,
        Field(
            alias="blockOwnerDeletion",
            description="""If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    controller: Annotated[
        bool | None,
        Field(
            description="""If true, this reference points to the managing controller.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str,
        Field(
            description="""Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ]

    name: Annotated[
        str,
        Field(
            description="""Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names"""
        ),
    ]

    uid: Annotated[
        str,
        Field(
            description="""UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids"""
        ),
    ]
