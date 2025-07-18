from .list_calendar_acl_response_body import ListCalendarAclResponseBody as ListCalendarAclResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCalendarAclResponse(BaseResponse):
    data: ListCalendarAclResponseBody | None
    def __init__(self, d=None) -> None: ...
