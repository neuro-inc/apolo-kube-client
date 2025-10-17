from pydantic import AliasChoices, BaseModel, Field
from .v1_api_service_spec import V1APIServiceSpec
from .v1_api_service_status import V1APIServiceStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1APIService",)


class V1APIService(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1APIServiceSpec = Field(default_factory=lambda: V1APIServiceSpec())

    status: V1APIServiceStatus = Field(default_factory=lambda: V1APIServiceStatus())
