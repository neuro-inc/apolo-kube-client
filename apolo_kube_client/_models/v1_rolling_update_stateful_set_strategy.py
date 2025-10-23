from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1RollingUpdateStatefulSetStrategy",)


class V1RollingUpdateStatefulSetStrategy(BaseModel):
    max_unavailable: JsonType = Field(
        default={},
        serialization_alias="maxUnavailable",
        validation_alias=AliasChoices("max_unavailable", "maxUnavailable"),
        exclude_if=_exclude_if,
    )

    partition: int | None = Field(default=None, exclude_if=_exclude_if)
