from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ContainerResizePolicy",)


class V1ContainerResizePolicy(BaseModel):
    resource_name: str | None = Field(
        default=None,
        serialization_alias="resourceName",
        validation_alias=AliasChoices("resource_name", "resourceName"),
        exclude_if=_exclude_if,
    )

    restart_policy: str | None = Field(
        default=None,
        serialization_alias="restartPolicy",
        validation_alias=AliasChoices("restart_policy", "restartPolicy"),
        exclude_if=_exclude_if,
    )
