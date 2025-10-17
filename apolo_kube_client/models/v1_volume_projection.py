from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_cluster_trust_bundle_projection import V1ClusterTrustBundleProjection
from .v1_config_map_projection import V1ConfigMapProjection
from .v1_downward_api_projection import V1DownwardAPIProjection
from .v1_pod_certificate_projection import V1PodCertificateProjection
from .v1_secret_projection import V1SecretProjection
from .v1_service_account_token_projection import V1ServiceAccountTokenProjection

__all__ = ("V1VolumeProjection",)


class V1VolumeProjection(BaseModel):
    cluster_trust_bundle: V1ClusterTrustBundleProjection = Field(
        default_factory=lambda: V1ClusterTrustBundleProjection(),
        alias="clusterTrustBundle",
    )

    config_map: V1ConfigMapProjection = Field(
        default_factory=lambda: V1ConfigMapProjection(), alias="configMap"
    )

    downward_api: V1DownwardAPIProjection = Field(
        default_factory=lambda: V1DownwardAPIProjection(), alias="downwardAPI"
    )

    pod_certificate: V1PodCertificateProjection = Field(
        default_factory=lambda: V1PodCertificateProjection(), alias="podCertificate"
    )

    secret: V1SecretProjection = Field(default_factory=lambda: V1SecretProjection())

    service_account_token: V1ServiceAccountTokenProjection = Field(
        default_factory=lambda: V1ServiceAccountTokenProjection(),
        alias="serviceAccountToken",
    )
