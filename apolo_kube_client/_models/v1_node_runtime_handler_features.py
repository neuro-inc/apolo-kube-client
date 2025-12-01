from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1NodeRuntimeHandlerFeatures",)


class V1NodeRuntimeHandlerFeatures(BaseModel):
    """NodeRuntimeHandlerFeatures is a set of features implemented by the runtime handler."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.NodeRuntimeHandlerFeatures"
    )

    recursive_read_only_mounts: Annotated[
        bool | None,
        Field(
            alias="recursiveReadOnlyMounts",
            description="""RecursiveReadOnlyMounts is set to true if the runtime handler supports RecursiveReadOnlyMounts.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    user_namespaces: Annotated[
        bool | None,
        Field(
            alias="userNamespaces",
            description="""UserNamespaces is set to true if the runtime handler supports UserNamespaces, including for volumes.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
