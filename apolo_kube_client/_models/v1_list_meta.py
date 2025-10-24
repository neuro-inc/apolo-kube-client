from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ListMeta",)


class V1ListMeta(BaseModel):
    """ListMeta describes metadata that synthetic resources must have, including lists and various status objects. A resource may have only one of {ObjectMeta, ListMeta}."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta"
    )

    continue_: Annotated[
        str | None,
        Field(
            alias="continue",
            description="""continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    remaining_item_count: Annotated[
        int | None,
        Field(
            alias="remainingItemCount",
            description="""remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource_version: Annotated[
        str | None,
        Field(
            alias="resourceVersion",
            description="""String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    self_link: Annotated[
        str | None,
        Field(
            alias="selfLink",
            description="""Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
