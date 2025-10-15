from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector


class V1ClusterTrustBundleProjection(BaseModel):
    label_selector: V1LabelSelector | None = Field(None, alias="labelSelector")

    name: str | None = Field(None, alias="name")

    optional: bool | None = Field(None, alias="optional")

    path: str | None = Field(None, alias="path")

    signer_name: str | None = Field(None, alias="signerName")
