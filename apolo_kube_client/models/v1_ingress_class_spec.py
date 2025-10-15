from pydantic import BaseModel, Field

from .v1_ingress_class_parameters_reference import V1IngressClassParametersReference


class V1IngressClassSpec(BaseModel):
    controller: str | None = Field(None, alias="controller")

    parameters: V1IngressClassParametersReference | None = Field(
        None, alias="parameters"
    )
