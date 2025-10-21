from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ClusterTrustBundleProjection",)


class V1ClusterTrustBundleProjection(BaseModel):
    label_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="labelSelector",
        validation_alias=AliasChoices("label_selector", "labelSelector"),
    )

    name: str | None = None

    optional: bool | None = None

    path: str | None = None

    signer_name: str | None = Field(
        default=None,
        serialization_alias="signerName",
        validation_alias=AliasChoices("signer_name", "signerName"),
    )
