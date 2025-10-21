from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator
from typing import Annotated

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

    selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(default_factory=lambda: V1LabelSelector())
