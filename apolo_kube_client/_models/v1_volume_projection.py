from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_cluster_trust_bundle_projection import V1ClusterTrustBundleProjection
from .v1_config_map_projection import V1ConfigMapProjection
from .v1_downward_api_projection import V1DownwardAPIProjection
from .v1_pod_certificate_projection import V1PodCertificateProjection
from .v1_secret_projection import V1SecretProjection
from .v1_service_account_token_projection import V1ServiceAccountTokenProjection
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1VolumeProjection",)


class V1VolumeProjection(BaseModel):
    cluster_trust_bundle: Annotated[
        V1ClusterTrustBundleProjection,
        BeforeValidator(_default_if_none(V1ClusterTrustBundleProjection)),
    ] = Field(
        default_factory=lambda: V1ClusterTrustBundleProjection(),
        serialization_alias="clusterTrustBundle",
        validation_alias=AliasChoices("cluster_trust_bundle", "clusterTrustBundle"),
        exclude_if=_exclude_if,
    )

    config_map: Annotated[
        V1ConfigMapProjection, BeforeValidator(_default_if_none(V1ConfigMapProjection))
    ] = Field(
        default_factory=lambda: V1ConfigMapProjection(),
        serialization_alias="configMap",
        validation_alias=AliasChoices("config_map", "configMap"),
        exclude_if=_exclude_if,
    )

    downward_api: Annotated[
        V1DownwardAPIProjection,
        BeforeValidator(_default_if_none(V1DownwardAPIProjection)),
    ] = Field(
        default_factory=lambda: V1DownwardAPIProjection(),
        serialization_alias="downwardAPI",
        validation_alias=AliasChoices("downward_api", "downwardAPI"),
        exclude_if=_exclude_if,
    )

    pod_certificate: Annotated[
        V1PodCertificateProjection,
        BeforeValidator(_default_if_none(V1PodCertificateProjection)),
    ] = Field(
        default_factory=lambda: V1PodCertificateProjection(),
        serialization_alias="podCertificate",
        validation_alias=AliasChoices("pod_certificate", "podCertificate"),
        exclude_if=_exclude_if,
    )

    secret: Annotated[
        V1SecretProjection, BeforeValidator(_default_if_none(V1SecretProjection))
    ] = Field(default_factory=lambda: V1SecretProjection(), exclude_if=_exclude_if)

    service_account_token: Annotated[
        V1ServiceAccountTokenProjection,
        BeforeValidator(_default_if_none(V1ServiceAccountTokenProjection)),
    ] = Field(
        default_factory=lambda: V1ServiceAccountTokenProjection(),
        serialization_alias="serviceAccountToken",
        validation_alias=AliasChoices("service_account_token", "serviceAccountToken"),
        exclude_if=_exclude_if,
    )
