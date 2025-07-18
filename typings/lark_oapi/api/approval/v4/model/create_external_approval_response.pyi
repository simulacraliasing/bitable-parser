from .create_external_approval_response_body import CreateExternalApprovalResponseBody as CreateExternalApprovalResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExternalApprovalResponse(BaseResponse):
    data: CreateExternalApprovalResponseBody | None
    def __init__(self, d=None) -> None: ...
