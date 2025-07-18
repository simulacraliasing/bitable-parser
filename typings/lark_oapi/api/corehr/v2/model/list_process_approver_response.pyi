from .list_process_approver_response_body import ListProcessApproverResponseBody as ListProcessApproverResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListProcessApproverResponse(BaseResponse):
    data: ListProcessApproverResponseBody | None
    def __init__(self, d=None) -> None: ...
