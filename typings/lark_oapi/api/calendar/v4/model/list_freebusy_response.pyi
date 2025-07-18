from .list_freebusy_response_body import ListFreebusyResponseBody as ListFreebusyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListFreebusyResponse(BaseResponse):
    data: ListFreebusyResponseBody | None
    def __init__(self, d=None) -> None: ...
