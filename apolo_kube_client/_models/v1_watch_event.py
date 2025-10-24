from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import KubeMeta
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1WatchEvent",)


class V1WatchEvent(BaseModel):
    """Event represents a single event to a watched resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.WatchEvent"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = (
        KubeMeta(group="", kind="WatchEvent", version="v1"),
        KubeMeta(group="admission.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="admission.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="admissionregistration.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(
            group="admissionregistration.k8s.io", kind="WatchEvent", version="v1alpha1"
        ),
        KubeMeta(
            group="admissionregistration.k8s.io", kind="WatchEvent", version="v1beta1"
        ),
        KubeMeta(group="apiextensions.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="apiextensions.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="apiregistration.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="apiregistration.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="apps", kind="WatchEvent", version="v1"),
        KubeMeta(group="apps", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="apps", kind="WatchEvent", version="v1beta2"),
        KubeMeta(group="authentication.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="authentication.k8s.io", kind="WatchEvent", version="v1alpha1"),
        KubeMeta(group="authentication.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="authorization.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="authorization.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="autoscaling", kind="WatchEvent", version="v1"),
        KubeMeta(group="autoscaling", kind="WatchEvent", version="v2"),
        KubeMeta(group="autoscaling", kind="WatchEvent", version="v2beta1"),
        KubeMeta(group="autoscaling", kind="WatchEvent", version="v2beta2"),
        KubeMeta(group="batch", kind="WatchEvent", version="v1"),
        KubeMeta(group="batch", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="certificates.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="certificates.k8s.io", kind="WatchEvent", version="v1alpha1"),
        KubeMeta(group="certificates.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="coordination.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="coordination.k8s.io", kind="WatchEvent", version="v1alpha2"),
        KubeMeta(group="coordination.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="discovery.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="discovery.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="events.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="events.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="extensions", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="flowcontrol.apiserver.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(
            group="flowcontrol.apiserver.k8s.io", kind="WatchEvent", version="v1beta1"
        ),
        KubeMeta(
            group="flowcontrol.apiserver.k8s.io", kind="WatchEvent", version="v1beta2"
        ),
        KubeMeta(
            group="flowcontrol.apiserver.k8s.io", kind="WatchEvent", version="v1beta3"
        ),
        KubeMeta(group="imagepolicy.k8s.io", kind="WatchEvent", version="v1alpha1"),
        KubeMeta(
            group="internal.apiserver.k8s.io", kind="WatchEvent", version="v1alpha1"
        ),
        KubeMeta(group="networking.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="networking.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="node.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="node.k8s.io", kind="WatchEvent", version="v1alpha1"),
        KubeMeta(group="node.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="policy", kind="WatchEvent", version="v1"),
        KubeMeta(group="policy", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="rbac.authorization.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(
            group="rbac.authorization.k8s.io", kind="WatchEvent", version="v1alpha1"
        ),
        KubeMeta(
            group="rbac.authorization.k8s.io", kind="WatchEvent", version="v1beta1"
        ),
        KubeMeta(group="resource.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="resource.k8s.io", kind="WatchEvent", version="v1alpha3"),
        KubeMeta(group="resource.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="resource.k8s.io", kind="WatchEvent", version="v1beta2"),
        KubeMeta(group="scheduling.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="scheduling.k8s.io", kind="WatchEvent", version="v1alpha1"),
        KubeMeta(group="scheduling.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(group="storage.k8s.io", kind="WatchEvent", version="v1"),
        KubeMeta(group="storage.k8s.io", kind="WatchEvent", version="v1alpha1"),
        KubeMeta(group="storage.k8s.io", kind="WatchEvent", version="v1beta1"),
        KubeMeta(
            group="storagemigration.k8s.io", kind="WatchEvent", version="v1alpha1"
        ),
    )

    object: Annotated[
        JsonType,
        Field(
            description="""Object is:
 * If Type is Added or Modified: the new state of the object.
 * If Type is Deleted: the state of the object immediately before deletion.
 * If Type is Error: *Status is recommended; other types may make sense
   depending on context."""
        ),
    ]

    type: Annotated[str, Field()]
