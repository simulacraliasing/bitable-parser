from .list_tasklist_response_body import ListTasklistResponseBody as ListTasklistResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTasklistResponse(BaseResponse):
    data: ListTasklistResponseBody | None
    def __init__(self, d=None) -> None: ...
