from .create_calendar_acl_response_body import CreateCalendarAclResponseBody as CreateCalendarAclResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCalendarAclResponse(BaseResponse):
    data: CreateCalendarAclResponseBody | None
    def __init__(self, d=None) -> None: ...
