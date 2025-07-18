from .process_approval_info_response_body import ProcessApprovalInfoResponseBody as ProcessApprovalInfoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ProcessApprovalInfoResponse(BaseResponse):
    data: ProcessApprovalInfoResponseBody | None
    def __init__(self, d=None) -> None: ...
