from .list_process_response_body import ListProcessResponseBody as ListProcessResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListProcessResponse(BaseResponse):
    data: ListProcessResponseBody | None
    def __init__(self, d=None) -> None: ...
