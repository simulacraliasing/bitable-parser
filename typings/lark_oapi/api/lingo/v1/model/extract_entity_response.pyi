from .extract_entity_response_body import ExtractEntityResponseBody as ExtractEntityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ExtractEntityResponse(BaseResponse):
    data: ExtractEntityResponseBody | None
    def __init__(self, d=None) -> None: ...
