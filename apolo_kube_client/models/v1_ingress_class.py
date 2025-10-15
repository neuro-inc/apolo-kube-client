from pydantic import BaseModel, Field

from .v1_ingress_class_spec import V1IngressClassSpec
from .v1_object_meta import V1ObjectMeta


class V1IngressClass(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1IngressClassSpec | None = Field(None, alias="spec")
