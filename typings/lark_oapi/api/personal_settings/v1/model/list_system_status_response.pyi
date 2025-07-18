from .list_system_status_response_body import ListSystemStatusResponseBody as ListSystemStatusResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSystemStatusResponse(BaseResponse):
    data: ListSystemStatusResponseBody | None
    def __init__(self, d=None) -> None: ...
