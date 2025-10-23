from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_managed_fields_entry import V1ManagedFieldsEntry
from .v1_owner_reference import V1OwnerReference
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ObjectMeta",)


class V1ObjectMeta(BaseModel):
    annotations: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(default={}, exclude_if=_exclude_if)

    creation_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="creationTimestamp",
        validation_alias=AliasChoices("creation_timestamp", "creationTimestamp"),
        exclude_if=_exclude_if,
    )

    deletion_grace_period_seconds: int | None = Field(
        default=None,
        serialization_alias="deletionGracePeriodSeconds",
        validation_alias=AliasChoices(
            "deletion_grace_period_seconds", "deletionGracePeriodSeconds"
        ),
        exclude_if=_exclude_if,
    )

    deletion_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="deletionTimestamp",
        validation_alias=AliasChoices("deletion_timestamp", "deletionTimestamp"),
        exclude_if=_exclude_if,
    )

    finalizers: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )

    generate_name: str | None = Field(
        default=None,
        serialization_alias="generateName",
        validation_alias=AliasChoices("generate_name", "generateName"),
        exclude_if=_exclude_if,
    )

    generation: int | None = Field(default=None, exclude_if=_exclude_if)

    labels: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = (
        Field(default={}, exclude_if=_exclude_if)
    )

    managed_fields: Annotated[
        list[V1ManagedFieldsEntry], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="managedFields",
        validation_alias=AliasChoices("managed_fields", "managedFields"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    namespace: str | None = Field(default=None, exclude_if=_exclude_if)

    owner_references: Annotated[
        list[V1OwnerReference], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="ownerReferences",
        validation_alias=AliasChoices("owner_references", "ownerReferences"),
        exclude_if=_exclude_if,
    )

    resource_version: str | None = Field(
        default=None,
        serialization_alias="resourceVersion",
        validation_alias=AliasChoices("resource_version", "resourceVersion"),
        exclude_if=_exclude_if,
    )

    self_link: str | None = Field(
        default=None,
        serialization_alias="selfLink",
        validation_alias=AliasChoices("self_link", "selfLink"),
        exclude_if=_exclude_if,
    )

    uid: str | None = Field(default=None, exclude_if=_exclude_if)
