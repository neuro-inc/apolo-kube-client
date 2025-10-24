from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ObjectReference",)


class V1ObjectReference(BaseModel):
    """ObjectReference contains enough information to let you inspect or modify the referred object."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ObjectReference"

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""API version of the referent.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    field_path: Annotated[
        str | None,
        Field(
            alias="fieldPath",
            description="""If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str | None,
        Field(
            description="""Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[
        str | None,
        Field(
            description="""Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    namespace: Annotated[
        str | None,
        Field(
            description="""Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource_version: Annotated[
        str | None,
        Field(
            alias="resourceVersion",
            description="""Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    uid: Annotated[
        str | None,
        Field(
            description="""UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
