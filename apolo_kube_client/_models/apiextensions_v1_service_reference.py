from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("ApiextensionsV1ServiceReference",)


class ApiextensionsV1ServiceReference(BaseModel):
    """ServiceReference holds a reference to Service.legacy.k8s.io"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.ServiceReference"
    )

    name: Annotated[
        str, Field(description="""name is the name of the service. Required""")
    ]

    namespace: Annotated[
        str,
        Field(description="""namespace is the namespace of the service. Required"""),
    ]

    path: Annotated[
        str | None,
        Field(
            description="""path is an optional URL path at which the webhook will be contacted.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    port: Annotated[
        int | None,
        Field(
            description="""port is an optional service port at which the webhook will be contacted. `port` should be a valid port number (1-65535, inclusive). Defaults to 443 for backward compatibility.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
