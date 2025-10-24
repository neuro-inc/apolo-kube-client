from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1beta1DeviceToleration",)


class V1beta1DeviceToleration(BaseModel):
    """The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta1.DeviceToleration"
    )

    effect: Annotated[
        str | None,
        Field(
            description="""Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    key: Annotated[
        str | None,
        Field(
            description="""Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    operator: Annotated[
        str | None,
        Field(
            description="""Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    toleration_seconds: Annotated[
        int | None,
        Field(
            alias="tolerationSeconds",
            description="""TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as <time when taint was adedd> + <toleration seconds>.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    value: Annotated[
        str | None,
        Field(
            description="""Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
