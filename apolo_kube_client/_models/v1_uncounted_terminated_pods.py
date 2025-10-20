from pydantic import BaseModel


__all__ = ("V1UncountedTerminatedPods",)


class V1UncountedTerminatedPods(BaseModel):
    failed: list[str] = []

    succeeded: list[str] = []
