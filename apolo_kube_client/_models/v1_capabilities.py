from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, BeforeValidator, Field

from .utils import _collection_if_none


__all__ = ("V1Capabilities",)


class V1Capabilities(BaseModel):
    """Adds and removes POSIX capabilities from running containers."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.Capabilities"

    add: Annotated[
        list[str],
        Field(description="""Added capabilities""", exclude_if=lambda v: v == []),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    drop: Annotated[
        list[str],
        Field(description="""Removed capabilities""", exclude_if=lambda v: v == []),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
