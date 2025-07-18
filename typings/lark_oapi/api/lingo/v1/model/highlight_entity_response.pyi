from .highlight_entity_response_body import HighlightEntityResponseBody as HighlightEntityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class HighlightEntityResponse(BaseResponse):
    data: HighlightEntityResponseBody | None
    def __init__(self, d=None) -> None: ...
