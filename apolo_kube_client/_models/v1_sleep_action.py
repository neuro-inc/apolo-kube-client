from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1SleepAction",)


class V1SleepAction(BaseModel):
    """SleepAction describes a "sleep" action."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.SleepAction"

    seconds: Annotated[
        int, Field(description="""Seconds is the number of seconds to sleep.""")
    ]
