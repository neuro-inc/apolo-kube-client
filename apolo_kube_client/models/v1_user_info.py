from pydantic import BaseModel


__all__ = ("V1UserInfo",)


class V1UserInfo(BaseModel):
    extra: dict[str, list[str]] = {}

    groups: list[str] = []

    uid: str | None = None

    username: str | None = None
