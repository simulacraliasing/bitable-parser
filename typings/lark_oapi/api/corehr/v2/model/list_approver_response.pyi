from .list_approver_response_body import ListApproverResponseBody as ListApproverResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListApproverResponse(BaseResponse):
    data: ListApproverResponseBody | None
    def __init__(self, d=None) -> None: ...
