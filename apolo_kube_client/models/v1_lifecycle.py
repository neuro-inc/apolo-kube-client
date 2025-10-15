from pydantic import BaseModel, Field

from .v1_lifecycle_handler import V1LifecycleHandler


class V1Lifecycle(BaseModel):
    post_start: V1LifecycleHandler | None = Field(None, alias="postStart")

    pre_stop: V1LifecycleHandler | None = Field(None, alias="preStop")
