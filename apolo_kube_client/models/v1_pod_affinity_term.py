from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector


class V1PodAffinityTerm(BaseModel):
    label_selector: V1LabelSelector | None = Field(None, alias="labelSelector")

    match_label_keys: list[str] | None = Field(None, alias="matchLabelKeys")

    mismatch_label_keys: list[str] | None = Field(None, alias="mismatchLabelKeys")

    namespace_selector: V1LabelSelector | None = Field(None, alias="namespaceSelector")

    namespaces: list[str] | None = Field(None, alias="namespaces")

    topology_key: str | None = Field(None, alias="topologyKey")
