from .batch_query_agency_response_body import BatchQueryAgencyResponseBody as BatchQueryAgencyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchQueryAgencyResponse(BaseResponse):
    data: BatchQueryAgencyResponseBody | None
    def __init__(self, d=None) -> None: ...
