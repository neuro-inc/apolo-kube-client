from pydantic import AliasChoices, BaseModel, Field
from .v1_label_selector import V1LabelSelector

__all__ = ("V1alpha1ParamRef",)


class V1alpha1ParamRef(BaseModel):
    name: str | None = None

    namespace: str | None = None

    parameter_not_found_action: str | None = Field(
        default=None,
        serialization_alias="parameterNotFoundAction",
        validation_alias=AliasChoices(
            "parameter_not_found_action", "parameterNotFoundAction"
        ),
    )

    selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())
