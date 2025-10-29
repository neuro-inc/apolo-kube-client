from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_user_info import V1UserInfo
from pydantic import BeforeValidator

__all__ = ("V1SelfSubjectReviewStatus",)


class V1SelfSubjectReviewStatus(BaseModel):
    """SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authentication.v1.SelfSubjectReviewStatus"
    )

    user_info: Annotated[
        V1UserInfo,
        Field(
            alias="userInfo",
            description="""User attributes of the user making this request.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1UserInfo)),
    ] = V1UserInfo()
