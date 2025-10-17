from pydantic import BaseModel


__all__ = ("V1ConfigMapEnvSource",)


class V1ConfigMapEnvSource(BaseModel):
    name: str | None = None

    optional: bool | None = None
