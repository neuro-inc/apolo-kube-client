from apolo_kube_client._attr import _Attr
from apolo_kube_client._base_resource import Base, NamespacedResource
from apolo_kube_client._client import KubeClient
from apolo_kube_client._vcluster._attr_proxy import _AttrProxy
from apolo_kube_client._vcluster._client_proxy import KubeClientProxy
from apolo_kube_client._vcluster._resource_proxy import (
    BaseProxy,
    NamespacedResourceProxy,
)


def check_proxy(proxy: type, origin: type) -> None:
    origin_names = {
        name for name in dir(origin) if isinstance(getattr(origin, name), _Attr)
    }
    proxy_names = {
        name for name in dir(proxy) if isinstance(getattr(proxy, name), _AttrProxy)
    }
    assert proxy_names <= origin_names

    for name in proxy_names:
        orig_attr = getattr(origin, name)
        proxy_attr = getattr(proxy, name)

        assert issubclass(proxy_attr.cls, (BaseProxy, NamespacedResourceProxy))
        assert issubclass(orig_attr.cls, (Base, NamespacedResource))


def test_compliance() -> None:
    check_proxy(KubeClientProxy, KubeClient)
