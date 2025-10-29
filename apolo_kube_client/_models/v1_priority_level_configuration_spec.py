from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_exempt_priority_level_configuration import V1ExemptPriorityLevelConfiguration
from .v1_limited_priority_level_configuration import V1LimitedPriorityLevelConfiguration
from pydantic import BeforeValidator

__all__ = ("V1PriorityLevelConfigurationSpec",)


class V1PriorityLevelConfigurationSpec(BaseModel):
    """PriorityLevelConfigurationSpec specifies the configuration of a priority level."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationSpec"
    )

    exempt: Annotated[
        V1ExemptPriorityLevelConfiguration,
        Field(
            description="""`exempt` specifies how requests are handled for an exempt priority level. This field MUST be empty if `type` is `"Limited"`. This field MAY be non-empty if `type` is `"Exempt"`. If empty and `type` is `"Exempt"` then the default values for `ExemptPriorityLevelConfiguration` apply.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ExemptPriorityLevelConfiguration)),
    ] = V1ExemptPriorityLevelConfiguration()

    limited: Annotated[
        V1LimitedPriorityLevelConfiguration,
        Field(
            description="""`limited` specifies how requests are handled for a Limited priority level. This field must be non-empty if and only if `type` is `"Limited"`.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LimitedPriorityLevelConfiguration)),
    ] = V1LimitedPriorityLevelConfiguration()

    type: Annotated[
        str,
        Field(
            description="""`type` indicates whether this priority level is subject to limitation on request execution.  A value of `"Exempt"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `"Limited"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required."""
        ),
    ]
