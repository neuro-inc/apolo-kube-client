from pydantic import BaseModel, Field

from .v1_ingress_backend import V1IngressBackend


class V1HTTPIngressPath(BaseModel):
    backend: V1IngressBackend | None = Field(None, alias="backend")

    path: str | None = Field(None, alias="path")

    path_type: str | None = Field(None, alias="pathType")
