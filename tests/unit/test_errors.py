from apolo_kube_client._errors import _raise_for_obj, _raise_for_text
import pytest
from apolo_kube_client import (
    ResourceNotFound,
    V1Status,
    KubeClientException,
    ResourceGone,
)


def test_raise_for_obj_status() -> None:
    err = V1Status(code=404, message="error-text")
    with pytest.raises(ResourceNotFound) as e:
        _raise_for_obj(err.model_dump(mode="json"))

    assert e.value.args[0] == err


def test_raise_for_obj_generic() -> None:
    err = V1Status(code=0, message="error-text")
    with pytest.raises(KubeClientException) as e:
        _raise_for_obj(err.model_dump(mode="json"))

    assert e.value.args[0] == err


def test_raise_for_obj_unknown() -> None:
    err = 1234
    with pytest.raises(KubeClientException) as e:
        _raise_for_obj(err)  # type: ignore[arg-type]

    assert e.value.args[0] == err


def test_raise_for_text_status() -> None:
    err = V1Status(code=404, message="error-text")
    with pytest.raises(ResourceNotFound) as e:
        _raise_for_text(404, err.model_dump_json())

    assert e.value.args[0] == err


def test_raise_for_text_status_overrride_by_code() -> None:
    err = V1Status(code=404, message="error-text")
    with pytest.raises(ResourceNotFound) as e:
        _raise_for_text(400, err.model_dump_json())

    assert e.value.args[0] == err


def test_raise_for_text_generic() -> None:
    err = V1Status(code=0, message="error-text")
    with pytest.raises(KubeClientException) as e:
        _raise_for_text(400, err.model_dump_json())

    assert e.value.args[0] == err


def test_raise_for_text_unknown() -> None:
    err = "err-text"
    with pytest.raises(ResourceGone) as e:
        _raise_for_text(410, err)

    assert e.value.args[0] == err
