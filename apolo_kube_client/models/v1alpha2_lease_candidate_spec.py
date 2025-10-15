from datetime import datetime

from pydantic import BaseModel, Field


class V1alpha2LeaseCandidateSpec(BaseModel):
    binary_version: str | None = Field(None, alias="binaryVersion")

    emulation_version: str | None = Field(None, alias="emulationVersion")

    lease_name: str | None = Field(None, alias="leaseName")

    ping_time: datetime | None = Field(None, alias="pingTime")

    renew_time: datetime | None = Field(None, alias="renewTime")

    strategy: str | None = Field(None, alias="strategy")
