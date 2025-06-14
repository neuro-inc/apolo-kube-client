def escape_json_pointer(path: str) -> str:
    """
    Escapes ~ and / in a JSON Pointer path according to RFC 6901.
    Replaces ~ with ~0 and / with ~1.
    """
    return path.replace("~", "~0").replace("/", "~1")
