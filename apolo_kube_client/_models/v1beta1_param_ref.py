from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1ParamRef",)


class V1beta1ParamRef(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    namespace: str | None = Field(default=None, exclude_if=_exclude_if)

    parameter_not_found_action: str | None = Field(
        default=None,
        serialization_alias="parameterNotFoundAction",
        validation_alias=AliasChoices(
            "parameter_not_found_action", "parameterNotFoundAction"
        ),
        exclude_if=_exclude_if,
    )

    selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(default_factory=lambda: V1LabelSelector(), exclude_if=_exclude_if)
