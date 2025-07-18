from .query_tenant_product_assign_info_response_body import QueryTenantProductAssignInfoResponseBody as QueryTenantProductAssignInfoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryTenantProductAssignInfoResponse(BaseResponse):
    data: QueryTenantProductAssignInfoResponseBody | None
    def __init__(self, d=None) -> None: ...
