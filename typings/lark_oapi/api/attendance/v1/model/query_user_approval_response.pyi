from .query_user_approval_response_body import QueryUserApprovalResponseBody as QueryUserApprovalResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserApprovalResponse(BaseResponse):
    data: QueryUserApprovalResponseBody | None
    def __init__(self, d=None) -> None: ...
