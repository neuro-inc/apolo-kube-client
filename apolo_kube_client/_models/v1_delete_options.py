from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import KubeMeta
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_preconditions import V1Preconditions
from pydantic import BeforeValidator

__all__ = ("V1DeleteOptions",)


class V1DeleteOptions(BaseModel):
    """DeleteOptions may be provided when deleting an API object."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.DeleteOptions"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = (
        KubeMeta(group="", kind="DeleteOptions", version="v1"),
        KubeMeta(group="admission.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="admission.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(
            group="admissionregistration.k8s.io", kind="DeleteOptions", version="v1"
        ),
        KubeMeta(
            group="admissionregistration.k8s.io",
            kind="DeleteOptions",
            version="v1alpha1",
        ),
        KubeMeta(
            group="admissionregistration.k8s.io",
            kind="DeleteOptions",
            version="v1beta1",
        ),
        KubeMeta(group="apiextensions.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="apiextensions.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="apiregistration.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(
            group="apiregistration.k8s.io", kind="DeleteOptions", version="v1beta1"
        ),
        KubeMeta(group="apps", kind="DeleteOptions", version="v1"),
        KubeMeta(group="apps", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="apps", kind="DeleteOptions", version="v1beta2"),
        KubeMeta(group="authentication.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(
            group="authentication.k8s.io", kind="DeleteOptions", version="v1alpha1"
        ),
        KubeMeta(
            group="authentication.k8s.io", kind="DeleteOptions", version="v1beta1"
        ),
        KubeMeta(group="authorization.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="authorization.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="autoscaling", kind="DeleteOptions", version="v1"),
        KubeMeta(group="autoscaling", kind="DeleteOptions", version="v2"),
        KubeMeta(group="autoscaling", kind="DeleteOptions", version="v2beta1"),
        KubeMeta(group="autoscaling", kind="DeleteOptions", version="v2beta2"),
        KubeMeta(group="batch", kind="DeleteOptions", version="v1"),
        KubeMeta(group="batch", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="certificates.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="certificates.k8s.io", kind="DeleteOptions", version="v1alpha1"),
        KubeMeta(group="certificates.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="coordination.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="coordination.k8s.io", kind="DeleteOptions", version="v1alpha2"),
        KubeMeta(group="coordination.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="discovery.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="discovery.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="events.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="events.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="extensions", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(
            group="flowcontrol.apiserver.k8s.io", kind="DeleteOptions", version="v1"
        ),
        KubeMeta(
            group="flowcontrol.apiserver.k8s.io",
            kind="DeleteOptions",
            version="v1beta1",
        ),
        KubeMeta(
            group="flowcontrol.apiserver.k8s.io",
            kind="DeleteOptions",
            version="v1beta2",
        ),
        KubeMeta(
            group="flowcontrol.apiserver.k8s.io",
            kind="DeleteOptions",
            version="v1beta3",
        ),
        KubeMeta(group="imagepolicy.k8s.io", kind="DeleteOptions", version="v1alpha1"),
        KubeMeta(
            group="internal.apiserver.k8s.io", kind="DeleteOptions", version="v1alpha1"
        ),
        KubeMeta(group="networking.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="networking.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="node.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="node.k8s.io", kind="DeleteOptions", version="v1alpha1"),
        KubeMeta(group="node.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="policy", kind="DeleteOptions", version="v1"),
        KubeMeta(group="policy", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="rbac.authorization.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(
            group="rbac.authorization.k8s.io", kind="DeleteOptions", version="v1alpha1"
        ),
        KubeMeta(
            group="rbac.authorization.k8s.io", kind="DeleteOptions", version="v1beta1"
        ),
        KubeMeta(group="resource.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="resource.k8s.io", kind="DeleteOptions", version="v1alpha3"),
        KubeMeta(group="resource.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="resource.k8s.io", kind="DeleteOptions", version="v1beta2"),
        KubeMeta(group="scheduling.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="scheduling.k8s.io", kind="DeleteOptions", version="v1alpha1"),
        KubeMeta(group="scheduling.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(group="storage.k8s.io", kind="DeleteOptions", version="v1"),
        KubeMeta(group="storage.k8s.io", kind="DeleteOptions", version="v1alpha1"),
        KubeMeta(group="storage.k8s.io", kind="DeleteOptions", version="v1beta1"),
        KubeMeta(
            group="storagemigration.k8s.io", kind="DeleteOptions", version="v1alpha1"
        ),
    )

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    dry_run: Annotated[
        list[str],
        Field(
            alias="dryRun",
            description="""When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    grace_period_seconds: Annotated[
        int | None,
        Field(
            alias="gracePeriodSeconds",
            description="""The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    ignore_store_read_error_with_cluster_breaking_potential: Annotated[
        bool | None,
        Field(
            alias="ignoreStoreReadErrorWithClusterBreakingPotential",
            description="""if set to true, it will trigger an unsafe deletion of the resource in case the normal deletion flow fails with a corrupt object error. A resource is considered corrupt if it can not be retrieved from the underlying storage successfully because of a) its data can not be transformed e.g. decryption failure, or b) it fails to decode into an object. NOTE: unsafe deletion ignores finalizer constraints, skips precondition checks, and removes the object from the storage. WARNING: This may potentially break the cluster if the workload associated with the resource being unsafe-deleted relies on normal deletion flow. Use only if you REALLY know what you are doing. The default value is false, and the user must opt in to enable it""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str | None,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    orphan_dependents: Annotated[
        bool | None,
        Field(
            alias="orphanDependents",
            description="""Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the "orphan" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    preconditions: Annotated[
        V1Preconditions,
        Field(
            description="""Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1Preconditions)),
    ] = V1Preconditions()

    propagation_policy: Annotated[
        str | None,
        Field(
            alias="propagationPolicy",
            description="""Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
