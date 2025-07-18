from .get_message_response_body import GetMessageResponseBody as GetMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMessageResponse(BaseResponse):
    data: GetMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
