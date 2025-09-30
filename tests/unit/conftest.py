from collections.abc import Iterator
from unittest.mock import AsyncMock, patch

import pytest

pytest_plugins = [
    "tests.conftest_certs",
]


@pytest.fixture
def create_namespace_mock() -> Iterator[None]:
    with patch(
        "apolo_kube_client._vcluster._selector.create_namespace",
        return_value=AsyncMock(),
    ):
        yield
