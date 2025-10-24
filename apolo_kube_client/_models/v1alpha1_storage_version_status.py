from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1alpha1_server_storage_version import V1alpha1ServerStorageVersion
from .v1alpha1_storage_version_condition import V1alpha1StorageVersionCondition
from pydantic import BeforeValidator

__all__ = ("V1alpha1StorageVersionStatus",)


class V1alpha1StorageVersionStatus(BaseModel):
    """API server instances report the versions they can decode and the version they encode objects to when persisting objects in the backend."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.apiserverinternal.v1alpha1.StorageVersionStatus"
    )

    common_encoding_version: Annotated[
        str | None,
        Field(
            alias="commonEncodingVersion",
            description="""If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    conditions: Annotated[
        list[V1alpha1StorageVersionCondition],
        Field(
            description="""The latest available observations of the storageVersion's state.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    storage_versions: Annotated[
        list[V1alpha1ServerStorageVersion],
        Field(
            alias="storageVersions",
            description="""The reported versions per API server instance.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
