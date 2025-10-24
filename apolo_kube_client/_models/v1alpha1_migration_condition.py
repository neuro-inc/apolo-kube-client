from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1alpha1MigrationCondition",)


class V1alpha1MigrationCondition(BaseModel):
    """Describes the state of a migration at a certain point."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.storagemigration.v1alpha1.MigrationCondition"
    )

    last_update_time: Annotated[
        datetime | None,
        Field(
            alias="lastUpdateTime",
            description="""The last time this condition was updated.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""A human readable message indicating details about the transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""The reason for the condition's last transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        str,
        Field(description="""Status of the condition, one of True, False, Unknown."""),
    ]

    type: Annotated[str, Field(description="""Type of the condition.""")]
