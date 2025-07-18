from .query_recent_change_custom_org_response_body import QueryRecentChangeCustomOrgResponseBody as QueryRecentChangeCustomOrgResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRecentChangeCustomOrgResponse(BaseResponse):
    data: QueryRecentChangeCustomOrgResponseBody | None
    def __init__(self, d=None) -> None: ...
