from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _default_if_none
from .v1_client_ip_config import V1ClientIPConfig


__all__ = ("V1SessionAffinityConfig",)


class V1SessionAffinityConfig(BaseConfiguredModel):
    """SessionAffinityConfig represents the configurations of session affinity."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.SessionAffinityConfig"

    client_ip: Annotated[
        V1ClientIPConfig,
        Field(
            alias="clientIP",
            description="""clientIP contains the configurations of Client IP based session affinity.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ClientIPConfig)),
    ] = V1ClientIPConfig()
