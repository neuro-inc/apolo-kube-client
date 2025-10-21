from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourcePolicyRule",)


class V1ResourcePolicyRule(BaseModel):
    api_groups: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="apiGroups",
            validation_alias=AliasChoices("api_groups", "apiGroups"),
        )
    )

    cluster_scope: bool | None = Field(
        default=None,
        serialization_alias="clusterScope",
        validation_alias=AliasChoices("cluster_scope", "clusterScope"),
    )

    namespaces: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    resources: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    verbs: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
