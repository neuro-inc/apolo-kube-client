from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_non_resource_attributes import V1NonResourceAttributes
from .v1_resource_attributes import V1ResourceAttributes
from pydantic import BeforeValidator

__all__ = ("V1SelfSubjectAccessReviewSpec",)


class V1SelfSubjectAccessReviewSpec(BaseModel):
    """SelfSubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authorization.v1.SelfSubjectAccessReviewSpec"
    )

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
