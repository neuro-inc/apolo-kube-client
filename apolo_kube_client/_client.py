import logging
from types import TracebackType
from typing import Self, TypeVar, cast

from kubernetes.client import ApiClient

from ._batch_v1 import BatchV1Api
from ._config import KubeConfig
from ._core import _KubeCore
from ._core_v1 import CoreV1Api
from ._networking_k8s_io_v1 import NetworkingK8SioV1Api
from ._resource_list import ResourceListApi
from ._rest_response import _SimplifiedRestResponse
from ._typedefs import NestedStrKeyDict

logger = logging.getLogger(__name__)


ResourceModel = TypeVar("ResourceModel")


class KubeClient:
    def __init__(self, *, config: KubeConfig) -> None:
        self._core = _KubeCore(config)

        # Initialize the 3d party Official Kubernetes API client,
        # this is used only for deserialization raw responses for models
        self._api_client = ApiClient()

        self.resource_list = ResourceListApi(self._core, self._api_client)
        self.core_v1 = CoreV1Api(self._core, self._api_client)
        self.batch_v1 = BatchV1Api(self._core, self._api_client)
        self.networking_k8s_io_v1 = NetworkingK8SioV1Api(self._core, self._api_client)

    async def __aenter__(self) -> Self:
        await self._core.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self._core.__aexit__(exc_type=exc_type, exc_val=exc_val, exc_tb=exc_tb)

    @staticmethod
    def escape_json_pointer(path: str) -> str:
        """
        Escapes ~ and / in a JSON Pointer path according to RFC 6901.
        Replaces ~ with ~0 and / with ~1.
        """
        return path.replace("~", "~0").replace("/", "~1")

    def resource_dict_to_model(
        self,
        resource_dict: NestedStrKeyDict,
        response_type: ResourceModel,
    ) -> ResourceModel:
        """
        This method deserializes a resource dictionary into a specific resource model.
        """
        rest_response = _SimplifiedRestResponse(resource_dict)
        return cast(
            ResourceModel, self._api_client.deserialize(rest_response, response_type)
        )
