from pydantic import BaseModel, Field


class V1AzureFilePersistentVolumeSource(BaseModel):
    read_only: bool | None = Field(None, alias="readOnly")

    secret_name: str | None = Field(None, alias="secretName")

    secret_namespace: str | None = Field(None, alias="secretNamespace")

    share_name: str | None = Field(None, alias="shareName")
