import json
from types import TracebackType
from typing import Self

import aiohttp

from ._typedefs import NestedStrKeyDict


class _RESTResponse:
    """
    This is our custom analogue of the `kubernetes.client.rest.RESTResponse` class
    that is used for deserializing response data from the Kubernetes API.
    Aiohttp Response instead of the urllib3 Response
    """

    def __init__(self, resp: aiohttp.ClientResponse):
        self.response = resp
        self.status = resp.status
        self.reason = resp.reason

    async def __aenter__(self) -> Self:
        self.data = await self.response.read()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        pass


class _SimplifiedRestResponse:
    """
    This is simplified analogue of RestResponse is used to deserialize the response
    in official Kubernetes client, but only for dict-like objects.
    """

    def __init__(self, data: NestedStrKeyDict):
        self.data: bytes = json.dumps(data).encode()
