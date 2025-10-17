from pydantic import BaseModel


__all__ = ("V1FlowDistinguisherMethod",)


class V1FlowDistinguisherMethod(BaseModel):
    type: str | None = None
