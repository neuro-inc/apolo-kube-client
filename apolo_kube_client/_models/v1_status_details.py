from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_status_cause import V1StatusCause
from pydantic import BeforeValidator

__all__ = ("V1StatusDetails",)


class V1StatusDetails(BaseModel):
    """StatusDetails is a set of additional properties that MAY be set by the server to provide additional information about a response. The Reason field of a Status object defines what attributes will be set. Clients must ignore fields that do not match the defined type of each attribute, and should assume that any attribute may be empty, invalid, or under defined."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.StatusDetails"
    )

    causes: Annotated[
        list[V1StatusCause],
        Field(
            description="""The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    group: Annotated[
        str | None,
        Field(
            description="""The group attribute of the resource associated with the status StatusReason.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str | None,
        Field(
            description="""The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[
        str | None,
        Field(
            description="""The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    retry_after_seconds: Annotated[
        int | None,
        Field(
            alias="retryAfterSeconds",
            description="""If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    uid: Annotated[
        str | None,
        Field(
            description="""UID of the resource. (when there is a single resource which can be described). More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
