from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressTLS",)


class V1IngressTLS(BaseModel):
    hosts: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    secret_name: str | None = Field(
        default=None,
        serialization_alias="secretName",
        validation_alias=AliasChoices("secret_name", "secretName"),
    )
