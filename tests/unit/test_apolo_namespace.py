import string
from collections.abc import Iterator
from unittest.mock import Mock, patch

import pytest

from apolo_kube_client.apolo import (
    KUBE_NAME_LENGTH_MAX,
    KUBE_NAMESPACE_HASH_LENGTH,
    KUBE_NAMESPACE_PREFIX,
    KUBE_NAMESPACE_SEP,
    generate_namespace_name,
)


class TestGenerateNamespaceName:
    @pytest.fixture(scope="class")
    def hexdigest_mock(self) -> Iterator[str]:
        hexdigest_value = "h" * 32
        hexdigest_mock = Mock()
        hexdigest_mock.hexdigest.return_value = hexdigest_value

        with patch("apolo_kube_client.apolo.sha256", return_value=hexdigest_mock):
            yield hexdigest_value

    @pytest.mark.parametrize(
        ("org_name", "project_name", "expected"),
        [
            ("NO_ORG", "PROJECT_NAME", "no-org--project-name"),
            ("NO org", "PROJECT  NaMe", "no-org--project-name"),
            ("no:org", "project___:name", "no-org--project-name"),
            ("no\\org", "project\\name", "no-org--project-name"),
            ("no/org", "project/name", "no-org--project-name"),
            ("no/org", "project/name/one", "no-org--project-name-one"),
        ],
    )
    def test__ensure_illegal_chars_normalized(
        self,
        org_name: str,
        project_name: str,
        expected: str,
    ) -> None:
        actual_namespace_name = generate_namespace_name(org_name, project_name)
        assert expected in actual_namespace_name

    def test__name_does_not_exceed_threshold(
        self,
        hexdigest_mock: str,
    ) -> None:
        org_name, project_name = "org", "project"
        actual_namespace_name = generate_namespace_name(org_name, project_name)
        expected_namespace_name = (
            f"{KUBE_NAMESPACE_PREFIX}"
            f"{KUBE_NAMESPACE_SEP}"
            # we expect that org name will have 13 first characters,
            # while project name will have 12
            f"{org_name}"
            f"{KUBE_NAMESPACE_SEP}"
            f"{project_name}"
            f"{KUBE_NAMESPACE_SEP}"
            f"{hexdigest_mock[:KUBE_NAMESPACE_HASH_LENGTH]}"
        )
        assert expected_namespace_name == actual_namespace_name

    def test__name_exceeds_threshold__names_are_equal_length(
        self,
        hexdigest_mock: str,
    ) -> None:
        org_name = project_name = string.ascii_lowercase

        expected_namespace_name = (
            f"{KUBE_NAMESPACE_PREFIX}"
            f"{KUBE_NAMESPACE_SEP}"
            # we expect that org name will have 13 first characters,
            # while project name will have 12
            f"{string.ascii_lowercase[:12]}"
            f"{KUBE_NAMESPACE_SEP}"
            f"{string.ascii_lowercase[:13]}"
            f"{KUBE_NAMESPACE_SEP}"
            f"{hexdigest_mock[:KUBE_NAMESPACE_HASH_LENGTH]}"
        )
        actual_namespace_name = generate_namespace_name(org_name, project_name)
        assert actual_namespace_name == expected_namespace_name
        assert len(actual_namespace_name) == KUBE_NAME_LENGTH_MAX

    def test__name_exceeds_threshold__org_name_is_slightly_bigger(
        self, hexdigest_mock: str
    ) -> None:
        org_name = string.ascii_lowercase
        project_name = "p"

        expected_namespace_name = (
            f"{KUBE_NAMESPACE_PREFIX}"
            f"{KUBE_NAMESPACE_SEP}"
            f"{string.ascii_lowercase[:24]}"
            f"{KUBE_NAMESPACE_SEP}"
            f"p"
            f"{KUBE_NAMESPACE_SEP}"
            f"{hexdigest_mock[:KUBE_NAMESPACE_HASH_LENGTH]}"
        )
        actual_namespace_name = generate_namespace_name(org_name, project_name)
        assert actual_namespace_name == expected_namespace_name
        assert len(actual_namespace_name) == KUBE_NAME_LENGTH_MAX

    def test__name_exceeds_threshold__project_name_is_slightly_bigger(
        self, hexdigest_mock: str
    ) -> None:
        org_name = "o"
        project_name = string.ascii_lowercase

        expected_namespace_name = (
            f"{KUBE_NAMESPACE_PREFIX}"
            f"{KUBE_NAMESPACE_SEP}"
            f"o"
            f"{KUBE_NAMESPACE_SEP}"
            f"{string.ascii_lowercase[:24]}"
            f"{KUBE_NAMESPACE_SEP}"
            f"{hexdigest_mock[:KUBE_NAMESPACE_HASH_LENGTH]}"
        )
        actual_namespace_name = generate_namespace_name(org_name, project_name)
        assert actual_namespace_name == expected_namespace_name
        assert len(actual_namespace_name) == KUBE_NAME_LENGTH_MAX
