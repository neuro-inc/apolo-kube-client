from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1Overhead",)


class V1Overhead(BaseModel):
    """Overhead structure represents the resource overhead associated with running a pod."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.node.v1.Overhead"

    pod_fixed: Annotated[
        dict[str, str],
        Field(
            alias="podFixed",
            description="""podFixed represents the fixed resource overhead associated with running a pod.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}
