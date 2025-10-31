from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_custom_resource_definition_condition import V1CustomResourceDefinitionCondition
from .v1_custom_resource_definition_names import V1CustomResourceDefinitionNames
from pydantic import BeforeValidator

__all__ = ("V1CustomResourceDefinitionStatus",)


class V1CustomResourceDefinitionStatus(BaseModel):
    """CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionStatus"
    )

    accepted_names: Annotated[
        V1CustomResourceDefinitionNames | None,
        Field(
            alias="acceptedNames",
            description="""acceptedNames are the names that are actually being used to serve discovery. They may be different than the names in spec.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    conditions: Annotated[
        list[V1CustomResourceDefinitionCondition],
        Field(
            description="""conditions indicate state for particular aspects of a CustomResourceDefinition""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    stored_versions: Annotated[
        list[str],
        Field(
            alias="storedVersions",
            description="""storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from `spec.versions` while they exist in this list.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
