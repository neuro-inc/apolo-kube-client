from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, BeforeValidator, Field

from .utils import _collection_if_none


__all__ = ("V1HostAlias",)


class V1HostAlias(BaseModel):
    """HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.HostAlias"

    hostnames: Annotated[
        list[str],
        Field(
            description="""Hostnames for the above IP address.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    ip: Annotated[str, Field(description="""IP address of the host file entry.""")]
