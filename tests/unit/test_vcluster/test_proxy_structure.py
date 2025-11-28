from apolo_kube_client._attr import _Attr
from apolo_kube_client._base_resource import (
    Base,
    ClusterScopedResource,
    NamespacedResource,
)
from apolo_kube_client._client import KubeClient
from apolo_kube_client._vcluster._attr_proxy import _AttrProxy
from apolo_kube_client._vcluster._client_proxy import KubeClientProxy
from apolo_kube_client._vcluster._resource_proxy import (
    BaseProxy,
    ClusterScopedResourceProxy,
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
        assert proxy_attr.cls.__name__ == orig_attr.cls.__name__ + "Proxy"

        if issubclass(proxy_attr.cls, NamespacedResourceProxy):
            assert issubclass(proxy_attr.cls, NamespacedResourceProxy)
            assert issubclass(orig_attr.cls, NamespacedResource)
            func = proxy_attr.func
            assert func.__annotations__["return"] is orig_attr.cls
        elif issubclass(proxy_attr.cls, ClusterScopedResourceProxy):
            assert issubclass(proxy_attr.cls, ClusterScopedResourceProxy)
            assert issubclass(orig_attr.cls, ClusterScopedResource)
            func = proxy_attr.func
            assert func.__annotations__["return"] is orig_attr.cls
        else:
            assert issubclass(proxy_attr.cls, BaseProxy)
            assert issubclass(orig_attr.cls, Base)
            check_proxy(proxy_attr.cls, orig_attr.cls)


def test_compliance() -> None:
    check_proxy(KubeClientProxy, KubeClient)
