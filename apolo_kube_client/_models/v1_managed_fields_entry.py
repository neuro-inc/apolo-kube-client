from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from apolo_kube_client._typedefs import JsonType
from datetime import datetime

__all__ = ("V1ManagedFieldsEntry",)


class V1ManagedFieldsEntry(BaseModel):
    """ManagedFieldsEntry is a workflow-id, a FieldSet and the group version of the resource that the fieldset applies to."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.ManagedFieldsEntry"
    )

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    fields_type: Annotated[
        str | None,
        Field(
            alias="fieldsType",
            description='''FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"''',
            exclude_if=lambda v: v is None,
        ),
    ] = None

    fields_v1: Annotated[
        JsonType,
        Field(
            alias="fieldsV1",
            description="""FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.""",
            exclude_if=lambda v: v == {},
        ),
    ] = {}

    manager: Annotated[
        str | None,
        Field(
            description="""Manager is an identifier of the workflow managing these fields.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    operation: Annotated[
        str | None,
        Field(
            description="""Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    subresource: Annotated[
        str | None,
        Field(
            description="""Subresource is the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    time: Annotated[
        datetime | None,
        Field(
            description="""Time is the timestamp of when the ManagedFields entry was added. The timestamp will also be updated if a field is added, the manager changes any of the owned fields value or removes a field. The timestamp does not update when a field is removed from the entry because another manager took it over.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
