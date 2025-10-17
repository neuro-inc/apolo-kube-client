from pydantic import BaseModel


__all__ = ("V1SecretKeySelector",)


class V1SecretKeySelector(BaseModel):
    key: str | None = None

    name: str | None = None

    optional: bool | None = None
