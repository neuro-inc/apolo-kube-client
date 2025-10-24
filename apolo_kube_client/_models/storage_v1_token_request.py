from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("StorageV1TokenRequest",)


class StorageV1TokenRequest(BaseModel):
    """TokenRequest contains parameters of a service account token."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.storage.v1.TokenRequest"

    audience: Annotated[
        str,
        Field(
            description="""audience is the intended audience of the token in "TokenRequestSpec". It will default to the audiences of kube apiserver."""
        ),
    ]

    expiration_seconds: Annotated[
        int | None,
        Field(
            alias="expirationSeconds",
            description="""expirationSeconds is the duration of validity of the token in "TokenRequestSpec". It has the same default value of "ExpirationSeconds" in "TokenRequestSpec".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
