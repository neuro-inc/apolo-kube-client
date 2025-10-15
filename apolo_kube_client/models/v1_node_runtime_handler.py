from pydantic import BaseModel, Field

from .v1_node_runtime_handler_features import V1NodeRuntimeHandlerFeatures


class V1NodeRuntimeHandler(BaseModel):
    features: V1NodeRuntimeHandlerFeatures | None = Field(None, alias="features")

    name: str | None = Field(None, alias="name")
