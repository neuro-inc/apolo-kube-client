from pydantic import BaseModel, Field


class V1NodeRuntimeHandlerFeatures(BaseModel):
    recursive_read_only_mounts: bool | None = Field(
        None, alias="recursiveReadOnlyMounts"
    )

    user_namespaces: bool | None = Field(None, alias="userNamespaces")
