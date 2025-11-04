from ._typedefs import JsonType
from ._models.v1_status import V1Status
from pydantic import ValidationError
from typing import NoReturn


class KubeClientException(Exception):
    """Base kube client error"""


class ResourceNotFound(KubeClientException):
    pass


class ResourceInvalid(KubeClientException):
    pass


class ResourceExists(KubeClientException):
    pass


class ResourceBadRequest(KubeClientException):
    pass


class ResourceGone(KubeClientException):
    pass


class KubeClientUnauthorized(KubeClientException):
    pass


ERROR_CODES_MAPPING: dict[int, type[Exception]] = {
    400: ResourceBadRequest,
    401: KubeClientUnauthorized,
    403: KubeClientException,
    404: ResourceNotFound,
    409: ResourceExists,
    410: ResourceGone,
    422: ResourceInvalid,
}


def _raise_for_obj(obj: dict[str, JsonType]) -> NoReturn:
    try:
        err_model = V1Status.model_validate(obj)
    except ValidationError:
        raise KubeClientException(obj) from None
    if err_model.code is not None:
        exc_cls = ERROR_CODES_MAPPING.get(err_model.code, KubeClientException)
    else:
        exc_cls = KubeClientException
    raise exc_cls(err_model)


def _raise_for_text(code: int, txt: str) -> NoReturn:
    exc_cls = ERROR_CODES_MAPPING.get(code, KubeClientException)
    try:
        err_model = V1Status.model_validate_json(txt)
    except ValidationError:
        raise exc_cls(txt) from None
    else:
        if err_model.code is not None:
            exc_cls = ERROR_CODES_MAPPING.get(err_model.code, KubeClientException)
        raise exc_cls(err_model)
