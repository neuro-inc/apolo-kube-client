from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1beta2ResourcePool",)


class V1beta2ResourcePool(BaseModel):
    """ResourcePool describes the pool that ResourceSlices belong to."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta2.ResourcePool"

    generation: Annotated[
        int,
        Field(
            description="""Generation tracks the change in a pool over time. Whenever a driver changes something about one or more of the resources in a pool, it must change the generation in all ResourceSlices which are part of that pool. Consumers of ResourceSlices should only consider resources from the pool with the highest generation number. The generation may be reset by drivers, which should be fine for consumers, assuming that all ResourceSlices in a pool are updated to match or deleted.

Combined with ResourceSliceCount, this mechanism enables consumers to detect pools which are comprised of multiple ResourceSlices and are in an incomplete state."""
        ),
    ]

    name: Annotated[
        str,
        Field(
            description="""Name is used to identify the pool. For node-local devices, this is often the node name, but this is not required.

It must not be longer than 253 characters and must consist of one or more DNS sub-domains separated by slashes. This field is immutable."""
        ),
    ]

    resource_slice_count: Annotated[
        int,
        Field(
            alias="resourceSliceCount",
            description="""ResourceSliceCount is the total number of ResourceSlices in the pool at this generation number. Must be greater than zero.

Consumers can use this to check whether they have seen all ResourceSlices belonging to the same pool.""",
        ),
    ]
