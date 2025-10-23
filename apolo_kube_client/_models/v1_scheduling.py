from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_toleration import V1Toleration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Scheduling",)


class V1Scheduling(BaseModel):
    node_selector: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="nodeSelector",
        validation_alias=AliasChoices("node_selector", "nodeSelector"),
        exclude_if=_exclude_if,
    )

    tolerations: Annotated[
        list[V1Toleration], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
