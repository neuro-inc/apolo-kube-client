from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1GroupVersionForDiscovery",)


class V1GroupVersionForDiscovery(BaseModel):
    """GroupVersion contains the "group/version" and "version" string of a version. It is made a struct to keep extensibility."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.GroupVersionForDiscovery"
    )

    group_version: Annotated[
        str,
        Field(
            alias="groupVersion",
            description='''groupVersion specifies the API group and version in the form "group/version"''',
        ),
    ]

    version: Annotated[
        str,
        Field(
            description="""version specifies the version in the form of "version". This is to save the clients the trouble of splitting the GroupVersion."""
        ),
    ]
