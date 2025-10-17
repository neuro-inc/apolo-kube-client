from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1PodResourceClaim",)


class V1PodResourceClaim(BaseModel):
    name: str | None = None

    resource_claim_name: str | None = Field(
        default=None,
        serialization_alias="resourceClaimName",
        validation_alias=AliasChoices("resource_claim_name", "resourceClaimName"),
    )

    resource_claim_template_name: str | None = Field(
        default=None,
        serialization_alias="resourceClaimTemplateName",
        validation_alias=AliasChoices(
            "resource_claim_template_name", "resourceClaimTemplateName"
        ),
    )
