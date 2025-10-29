from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_non_resource_attributes import V1NonResourceAttributes
from .v1_resource_attributes import V1ResourceAttributes
from pydantic import BeforeValidator

__all__ = ("V1SubjectAccessReviewSpec",)


class V1SubjectAccessReviewSpec(BaseModel):
    """SubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authorization.v1.SubjectAccessReviewSpec"
    )

    extra: Annotated[
        dict[str, list[str]],
        Field(
            description="""Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    groups: Annotated[
        list[str],
        Field(
            description="""Groups is the groups you're testing for.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    non_resource_attributes: Annotated[
        V1NonResourceAttributes,
        Field(
            alias="nonResourceAttributes",
            description="""NonResourceAttributes describes information for a non-resource access request""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1NonResourceAttributes)),
    ] = V1NonResourceAttributes()

    resource_attributes: Annotated[
        V1ResourceAttributes,
        Field(
            alias="resourceAttributes",
            description="""ResourceAuthorizationAttributes describes information for a resource access request""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ResourceAttributes)),
    ] = V1ResourceAttributes()

    uid: Annotated[
        str | None,
        Field(
            description="""UID information about the requesting user.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    user: Annotated[
        str | None,
        Field(
            description="""User is the user you're testing for. If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
