from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none
from .v1_resource_health import V1ResourceHealth


__all__ = ("V1ResourceStatus",)


class V1ResourceStatus(BaseConfiguredModel):
    """ResourceStatus represents the status of a single resource allocated to a Pod."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ResourceStatus"

    name: Annotated[
        str,
        Field(
            description="""Name of the resource. Must be unique within the pod and in case of non-DRA resource, match one of the resources from the pod spec. For DRA resources, the value must be "claim:<claim_name>/<request>". When this status is reported about a container, the "claim_name" and "request" must match one of the claims of this container."""
        ),
    ]

    resources: Annotated[
        list[V1ResourceHealth],
        Field(
            description="""List of unique resources health. Each element in the list contains an unique resource ID and its health. At a minimum, for the lifetime of a Pod, resource ID must uniquely identify the resource allocated to the Pod on the Node. If other Pod on the same Node reports the status with the same resource ID, it must be the same resource they share. See ResourceID type definition for a specific format it has in various use cases.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
