from pydantic import BaseModel, Field

from .v1_local_object_reference import V1LocalObjectReference
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference


class V1ServiceAccount(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    automount_service_account_token: bool | None = Field(
        None, alias="automountServiceAccountToken"
    )

    image_pull_secrets: list[V1LocalObjectReference] | None = Field(
        None, alias="imagePullSecrets"
    )

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    secrets: list[V1ObjectReference] | None = Field(None, alias="secrets")
