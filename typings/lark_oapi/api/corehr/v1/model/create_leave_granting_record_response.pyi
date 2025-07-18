from .create_leave_granting_record_response_body import CreateLeaveGrantingRecordResponseBody as CreateLeaveGrantingRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateLeaveGrantingRecordResponse(BaseResponse):
    data: CreateLeaveGrantingRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
