from .list_message_response_body import ListMessageResponseBody as ListMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMessageResponse(BaseResponse):
    data: ListMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
