from .list_alert_response_body import ListAlertResponseBody as ListAlertResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAlertResponse(BaseResponse):
    data: ListAlertResponseBody | None
    def __init__(self, d=None) -> None: ...
