from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_cluster_trust_bundle_projection import V1ClusterTrustBundleProjection
from .v1_config_map_projection import V1ConfigMapProjection
from .v1_downward_api_projection import V1DownwardAPIProjection
from .v1_secret_projection import V1SecretProjection
from .v1_service_account_token_projection import V1ServiceAccountTokenProjection

__all__ = ("V1VolumeProjection",)


class V1VolumeProjection(BaseModel):
    cluster_trust_bundle: V1ClusterTrustBundleProjection | None = Field(
        None, alias="clusterTrustBundle"
    )

    config_map: V1ConfigMapProjection | None = Field(None, alias="configMap")

    downward_api: V1DownwardAPIProjection | None = Field(None, alias="downwardAPI")

    secret: V1SecretProjection | None = Field(None, alias="secret")

    service_account_token: V1ServiceAccountTokenProjection | None = Field(
        None, alias="serviceAccountToken"
    )
