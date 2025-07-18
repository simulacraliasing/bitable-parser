from .query_tenant_response_body import QueryTenantResponseBody as QueryTenantResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryTenantResponse(BaseResponse):
    data: QueryTenantResponseBody | None
    def __init__(self, d=None) -> None: ...
