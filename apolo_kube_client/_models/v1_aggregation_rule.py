from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none
from .v1_label_selector import V1LabelSelector


__all__ = ("V1AggregationRule",)


class V1AggregationRule(BaseConfiguredModel):
    """AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole"""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.rbac.v1.AggregationRule"

    cluster_role_selectors: Annotated[
        list[V1LabelSelector],
        Field(
            alias="clusterRoleSelectors",
            description="""ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
