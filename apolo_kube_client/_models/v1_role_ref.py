from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1RoleRef",)


class V1RoleRef(BaseModel):
    """RoleRef contains information that points to the role being used"""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.rbac.v1.RoleRef"

    api_group: Annotated[
        str,
        Field(
            alias="apiGroup",
            description="""APIGroup is the group for the resource being referenced""",
        ),
    ]

    kind: Annotated[
        str, Field(description="""Kind is the type of resource being referenced""")
    ]

    name: Annotated[
        str, Field(description="""Name is the name of resource being referenced""")
    ]
