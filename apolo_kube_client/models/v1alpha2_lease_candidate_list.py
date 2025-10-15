from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1alpha2_lease_candidate import V1alpha2LeaseCandidate


class V1alpha2LeaseCandidateList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1alpha2LeaseCandidate] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
