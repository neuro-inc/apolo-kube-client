from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("RbacV1Subject",)


class RbacV1Subject(BaseModel):
    """Subject contains a reference to the object or user identities a role binding applies to.  This can either hold a direct API object reference, or a value for non-objects such as user and group names."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.rbac.v1.Subject"

    api_group: Annotated[
        str | None,
        Field(
            alias="apiGroup",
            description="""APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str,
        Field(
            description="""Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error."""
        ),
    ]

    name: Annotated[str, Field(description="""Name of the object being referenced.""")]

    namespace: Annotated[
        str | None,
        Field(
            description="""Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
