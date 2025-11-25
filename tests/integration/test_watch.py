import asyncio

from apolo_kube_client import KubeClient, V1Node, Watch


class TestWatch:
    async def test_watch(self, kube_client: KubeClient) -> None:
        node_list = await kube_client.core_v1.node.get_list()
        node: V1Node = node_list.items[0]
        assert node.metadata.name is not None

        try:
            await kube_client.core_v1.node.patch_json(
                node.metadata.name,
                [{"op": "remove", "path": "/metadata/labels/test"}],
            )
        except Exception:
            pass

        started_event = asyncio.Event()
        watch: Watch[V1Node] | None = None

        async def _watch() -> None:
            nonlocal watch
            watch = kube_client.core_v1.node.watch()
            started_event.set()

            async for node_event in watch.stream():
                if (
                    node_event.type == "MODIFIED"
                    and node_event.object.metadata.labels["test"] == "test"
                ):
                    await asyncio.sleep(0.01)
                    break

        task = asyncio.create_task(_watch())

        await started_event.wait()

        await kube_client.core_v1.node.patch_json(
            node.metadata.name,
            [{"op": "add", "path": "/metadata/labels/test", "value": "test"}],
        )

        async with asyncio.timeout(5):
            await task

        assert watch is not None
        assert watch.resource_version is None

    async def test_watch__multiple_events(self, kube_client: KubeClient) -> None:
        node_list = await kube_client.core_v1.node.get_list()
        node: V1Node = node_list.items[0]
        assert node.metadata.name is not None

        try:
            await kube_client.core_v1.node.patch_json(
                node.metadata.name,
                [{"op": "remove", "path": "/metadata/labels/test"}],
            )
        except Exception:
            pass

        started_event = asyncio.Event()
        modified_event = asyncio.Event()
        max_events = 100
        events_count = 0

        async def _watch() -> None:
            watch = kube_client.core_v1.node.watch()
            started_event.set()

            async for node_event in watch.stream():
                nonlocal events_count

                if node_event.type == "MODIFIED" and node_event.object.metadata.labels[
                    "test"
                ].startswith("test"):
                    value = node_event.object.metadata.labels["test"]
                    if value == f"test-{events_count}":
                        modified_event.set()
                        events_count += 1
                    if events_count == max_events:
                        break

        task = asyncio.create_task(_watch())

        await started_event.wait()

        for i in range(max_events):
            await kube_client.core_v1.node.patch_json(
                node.metadata.name,
                [{"op": "add", "path": "/metadata/labels/test", "value": f"test-{i}"}],
            )
            await modified_event.wait()
            modified_event.clear()

        async with asyncio.timeout(5):
            await task

    async def test_update_resource_version(self, kube_client: KubeClient) -> None:
        node_list = await kube_client.core_v1.node.get_list()
        node: V1Node = node_list.items[0]
        assert node.metadata.name is not None

        try:
            await kube_client.core_v1.node.patch_json(
                node.metadata.name,
                [{"op": "remove", "path": "/metadata/labels/test"}],
            )
        except Exception:
            pass

        started_event = asyncio.Event()

        watch: Watch[V1Node] | None = None

        async def _watch() -> None:
            nonlocal watch
            watch = kube_client.core_v1.node.watch(allow_watch_bookmarks=True)
            started_event.set()

            async for node_event in watch.stream():
                if (
                    node_event.type == "MODIFIED"
                    and node_event.object.metadata.labels["test"] == "test"
                ):
                    await asyncio.sleep(0.01)
                    break

        task = asyncio.create_task(_watch())

        await started_event.wait()
        assert watch is not None
        assert watch.resource_version is None

        await kube_client.core_v1.node.patch_json(
            node.metadata.name,
            [{"op": "add", "path": "/metadata/labels/test", "value": "test"}],
        )

        async with asyncio.timeout(5):
            await task

        assert watch.resource_version is not None
