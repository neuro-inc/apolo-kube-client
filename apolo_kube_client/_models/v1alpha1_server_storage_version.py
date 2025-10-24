from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1alpha1ServerStorageVersion",)


class V1alpha1ServerStorageVersion(BaseModel):
    """An API server instance reports the version it can decode and the version it encodes objects to when persisting objects in the backend."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.apiserverinternal.v1alpha1.ServerStorageVersion"
    )

    api_server_id: Annotated[
        str | None,
        Field(
            alias="apiServerID",
            description="""The ID of the reporting API server.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    decodable_versions: Annotated[
        list[str],
        Field(
            alias="decodableVersions",
            description="""The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    encoding_version: Annotated[
        str | None,
        Field(
            alias="encodingVersion",
            description="""The API server encodes the object to this version when persisting it in the backend (e.g., etcd).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    served_versions: Annotated[
        list[str],
        Field(
            alias="servedVersions",
            description="""The API server can serve these versions. DecodableVersions must include all ServedVersions.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
