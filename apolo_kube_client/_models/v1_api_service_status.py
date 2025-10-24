from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_api_service_condition import V1APIServiceCondition
from pydantic import BeforeValidator

__all__ = ("V1APIServiceStatus",)


class V1APIServiceStatus(BaseModel):
    """APIServiceStatus contains derived information about an API server"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.kube-aggregator.pkg.apis.apiregistration.v1.APIServiceStatus"
    )

    conditions: Annotated[
        list[V1APIServiceCondition],
        Field(
            description="""Current service state of apiService.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
