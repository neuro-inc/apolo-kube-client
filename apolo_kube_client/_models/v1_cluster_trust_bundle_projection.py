from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator

__all__ = ("V1ClusterTrustBundleProjection",)


class V1ClusterTrustBundleProjection(BaseModel):
    """ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project their contents into the pod filesystem."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.ClusterTrustBundleProjection"
    )

    label_selector: Annotated[
        V1LabelSelector,
        Field(
            alias="labelSelector",
            description="""Select all ClusterTrustBundles that match this label selector.  Only has effect if signerName is set.  Mutually-exclusive with name.  If unset, interpreted as "match nothing".  If set but empty, interpreted as "match everything".""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LabelSelector)),
    ] = V1LabelSelector()

    name: Annotated[
        str | None,
        Field(
            description="""Select a single ClusterTrustBundle by object name.  Mutually-exclusive with signerName and labelSelector.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    optional: Annotated[
        bool | None,
        Field(
            description="""If true, don't block pod startup if the referenced ClusterTrustBundle(s) aren't available.  If using name, then the named ClusterTrustBundle is allowed not to exist.  If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    path: Annotated[
        str,
        Field(
            description="""Relative path from the volume root to write the bundle."""
        ),
    ]

    signer_name: Annotated[
        str | None,
        Field(
            alias="signerName",
            description="""Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name.  The contents of all selected ClusterTrustBundles will be unified and deduplicated.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
