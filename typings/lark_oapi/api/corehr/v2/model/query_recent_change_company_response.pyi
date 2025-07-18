from .query_recent_change_company_response_body import QueryRecentChangeCompanyResponseBody as QueryRecentChangeCompanyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRecentChangeCompanyResponse(BaseResponse):
    data: QueryRecentChangeCompanyResponseBody | None
    def __init__(self, d=None) -> None: ...
