from pydantic import BaseModel, Field


class V1NonResourceRule(BaseModel):
    non_resource_ur_ls: list[str] | None = Field(None, alias="nonResourceURLs")

    verbs: list[str] | None = Field(None, alias="verbs")
