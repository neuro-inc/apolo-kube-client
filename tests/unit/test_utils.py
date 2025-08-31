from apolo_kube_client._utils import escape_json_pointer


async def test_escape_json_pointer() -> None:
    # Test escaping of JSON pointers
    pointer = "/metadata/annotations~"
    escaped_pointer = escape_json_pointer(pointer)
    assert escaped_pointer == "~1metadata~1annotations~0"
