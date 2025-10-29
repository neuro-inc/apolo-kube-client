from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_client_ip_config import V1ClientIPConfig
from pydantic import BeforeValidator

__all__ = ("V1SessionAffinityConfig",)


class V1SessionAffinityConfig(BaseModel):
    """SessionAffinityConfig represents the configurations of session affinity."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

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
