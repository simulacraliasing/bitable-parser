from .update_process_approver_response_body import UpdateProcessApproverResponseBody as UpdateProcessApproverResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateProcessApproverResponse(BaseResponse):
    data: UpdateProcessApproverResponseBody | None
    def __init__(self, d=None) -> None: ...
