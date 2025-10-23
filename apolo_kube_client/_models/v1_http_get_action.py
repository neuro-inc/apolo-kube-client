from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_http_header import V1HTTPHeader
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1HTTPGetAction",)


class V1HTTPGetAction(BaseModel):
    host: str | None = Field(default=None, exclude_if=_exclude_if)

    http_headers: Annotated[
        list[V1HTTPHeader], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="httpHeaders",
        validation_alias=AliasChoices("http_headers", "httpHeaders"),
        exclude_if=_exclude_if,
    )

    path: str | None = Field(default=None, exclude_if=_exclude_if)

    port: JsonType = Field(default={}, exclude_if=_exclude_if)

    scheme: str | None = Field(default=None, exclude_if=_exclude_if)
