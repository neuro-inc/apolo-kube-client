from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1NonResourceRule",)


class V1NonResourceRule(BaseModel):
    """NonResourceRule holds information that describes a rule for the non-resource"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.authorization.v1.NonResourceRule"

    non_resource_ur_ls: Annotated[
        list[str],
        Field(
            alias="nonResourceURLs",
            description="""NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  "*" means all.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    verbs: Annotated[
        list[str],
        Field(
            description="""Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  "*" means all."""
        ),
    ]
