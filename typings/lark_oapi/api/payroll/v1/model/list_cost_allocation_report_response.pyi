from .list_cost_allocation_report_response_body import ListCostAllocationReportResponseBody as ListCostAllocationReportResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCostAllocationReportResponse(BaseResponse):
    data: ListCostAllocationReportResponseBody | None
    def __init__(self, d=None) -> None: ...
