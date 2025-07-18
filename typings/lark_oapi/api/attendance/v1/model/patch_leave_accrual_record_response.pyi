from .patch_leave_accrual_record_response_body import PatchLeaveAccrualRecordResponseBody as PatchLeaveAccrualRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchLeaveAccrualRecordResponse(BaseResponse):
    data: PatchLeaveAccrualRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
