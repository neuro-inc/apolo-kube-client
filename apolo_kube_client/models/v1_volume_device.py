from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1VolumeDevice",)


class V1VolumeDevice(BaseModel):
    device_path: str | None = Field(
        default=None,
        serialization_alias="devicePath",
        validation_alias=AliasChoices("device_path", "devicePath"),
    )

    name: str | None = None
