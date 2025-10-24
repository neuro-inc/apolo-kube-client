from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ResourceHealth",)


class V1ResourceHealth(BaseModel):
    """ResourceHealth represents the health of a resource. It has the latest device health information. This is a part of KEP https://kep.k8s.io/4680."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ResourceHealth"

    health: Annotated[
        str | None,
        Field(
            description="""Health of the resource. can be one of:
 - Healthy: operates as normal
 - Unhealthy: reported unhealthy. We consider this a temporary health issue
              since we do not have a mechanism today to distinguish
              temporary and permanent issues.
 - Unknown: The status cannot be determined.
            For example, Device Plugin got unregistered and hasn't been re-registered since.

In future we may want to introduce the PermanentlyUnhealthy Status.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource_id: Annotated[
        str,
        Field(
            alias="resourceID",
            description="""ResourceID is the unique identifier of the resource. See the ResourceID type for more information.""",
        ),
    ]
