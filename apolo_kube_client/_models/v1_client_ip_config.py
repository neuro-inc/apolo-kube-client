from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ClientIPConfig",)


class V1ClientIPConfig(BaseModel):
    """ClientIPConfig represents the configurations of Client IP based session affinity."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ClientIPConfig"

    timeout_seconds: Annotated[
        int | None,
        Field(
            alias="timeoutSeconds",
            description="""timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == "ClientIP". Default value is 10800(for 3 hours).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
