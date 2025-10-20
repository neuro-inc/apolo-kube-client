from pydantic import BaseModel


__all__ = ("V1TokenReviewSpec",)


class V1TokenReviewSpec(BaseModel):
    audiences: list[str] = []

    token: str | None = None
