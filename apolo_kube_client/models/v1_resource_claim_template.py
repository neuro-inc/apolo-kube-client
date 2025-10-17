from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_resource_claim_template_spec import V1ResourceClaimTemplateSpec

__all__ = ("V1ResourceClaimTemplate",)


class V1ResourceClaimTemplate(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1ResourceClaimTemplateSpec = Field(
        default_factory=lambda: V1ResourceClaimTemplateSpec()
    )
