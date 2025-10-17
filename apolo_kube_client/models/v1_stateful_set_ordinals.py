from pydantic import BaseModel


__all__ = ("V1StatefulSetOrdinals",)


class V1StatefulSetOrdinals(BaseModel):
    start: int | None = None
