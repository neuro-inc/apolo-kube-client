from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_rolling_update_daemon_set import V1RollingUpdateDaemonSet
from pydantic import BeforeValidator

__all__ = ("V1DaemonSetUpdateStrategy",)


class V1DaemonSetUpdateStrategy(BaseModel):
    """DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.DaemonSetUpdateStrategy"

    rolling_update: Annotated[
        V1RollingUpdateDaemonSet,
        Field(
            alias="rollingUpdate",
            description="""Rolling update config params. Present only if type = "RollingUpdate".""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1RollingUpdateDaemonSet)),
    ] = V1RollingUpdateDaemonSet()

    type: Annotated[
        str | None,
        Field(
            description="""Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
