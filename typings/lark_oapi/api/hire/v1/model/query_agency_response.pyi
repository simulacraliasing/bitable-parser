from .query_agency_response_body import QueryAgencyResponseBody as QueryAgencyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryAgencyResponse(BaseResponse):
    data: QueryAgencyResponseBody | None
    def __init__(self, d=None) -> None: ...
