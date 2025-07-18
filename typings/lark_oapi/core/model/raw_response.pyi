from lark_oapi.core.const import CONTENT_TYPE as CONTENT_TYPE

class RawResponse:
    status_code: int | None
    headers: dict[str, str]
    content: bytes | None
    def __init__(self) -> None: ...
    def set_content_type(self, content_type: str) -> None: ...
