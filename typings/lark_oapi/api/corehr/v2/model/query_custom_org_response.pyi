from .query_custom_org_response_body import QueryCustomOrgResponseBody as QueryCustomOrgResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryCustomOrgResponse(BaseResponse):
    data: QueryCustomOrgResponseBody | None
    def __init__(self, d=None) -> None: ...
