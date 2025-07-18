from .get_approval_response_body import GetApprovalResponseBody as GetApprovalResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetApprovalResponse(BaseResponse):
    data: GetApprovalResponseBody | None
    def __init__(self, d=None) -> None: ...
