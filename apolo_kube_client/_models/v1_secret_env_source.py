from pydantic import BaseModel


__all__ = ("V1SecretEnvSource",)


class V1SecretEnvSource(BaseModel):
    name: str | None = None

    optional: bool | None = None
