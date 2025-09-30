from pydantic import BaseModel


class V1DiskNamingCRDSpec(BaseModel):
    disk_id: str


class V1DiskNamingCRDMetadata(BaseModel):
    name: str
    namespace: str | None = None


class V1DiskNamingCRD(BaseModel):
    apiVersion: str = "neuromation.io/v1"
    kind: str = "DiskNaming"
    metadata: V1DiskNamingCRDMetadata
    spec: V1DiskNamingCRDSpec


class V1DiskNamingCRDList(BaseModel):
    apiVersion: str = "neuromation.io/v1"
    kind: str = "DiskNamingsList"
    items: list[V1DiskNamingCRD]
