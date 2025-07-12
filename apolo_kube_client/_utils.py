import base64


def escape_json_pointer(path: str) -> str:
    """
    Escapes ~ and / in a JSON Pointer path according to RFC 6901.
    Replaces ~ with ~0 and / with ~1.
    """
    return path.replace("~", "~0").replace("/", "~1")


def base64_encode(data: str) -> str:
    """Helper function to base64 encode a string."""
    return base64.b64encode(data.encode()).decode()


def base64_decode(data: str) -> str:
    """Helper function to base64 decode a string."""
    return base64.b64decode(data.encode()).decode()
