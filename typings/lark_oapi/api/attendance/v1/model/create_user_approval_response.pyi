from .create_user_approval_response_body import CreateUserApprovalResponseBody as CreateUserApprovalResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateUserApprovalResponse(BaseResponse):
    data: CreateUserApprovalResponseBody | None
    def __init__(self, d=None) -> None: ...
