from pydantic import BaseModel, ConfigDict


class BaseConfiguredModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )
