from .get_leave_employ_expire_record_response_body import GetLeaveEmployExpireRecordResponseBody as GetLeaveEmployExpireRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetLeaveEmployExpireRecordResponse(BaseResponse):
    data: GetLeaveEmployExpireRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
