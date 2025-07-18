from .get_external_approval_response_body import GetExternalApprovalResponseBody as GetExternalApprovalResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetExternalApprovalResponse(BaseResponse):
    data: GetExternalApprovalResponseBody | None
    def __init__(self, d=None) -> None: ...
