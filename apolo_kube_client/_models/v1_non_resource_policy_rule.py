from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1NonResourcePolicyRule",)


class V1NonResourcePolicyRule(BaseModel):
    """NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.NonResourcePolicyRule"
    )

    non_resource_ur_ls: Annotated[
        list[str],
        Field(
            alias="nonResourceURLs",
            description="""`nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example:
  - "/healthz" is legal
  - "/hea*" is illegal
  - "/hea" is legal but matches nothing
  - "/hea/*" also matches nothing
  - "/healthz/*" matches all per-component health checks.
"*" matches all non-resource urls. if it is present, it must be the only entry. Required.""",
        ),
    ]

    verbs: Annotated[
        list[str],
        Field(
            description="""`verbs` is a list of matching verbs and may not be empty. "*" matches all verbs. If it is present, it must be the only entry. Required."""
        ),
    ]
