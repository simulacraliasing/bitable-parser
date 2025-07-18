from .query_recent_change_job_family_response_body import QueryRecentChangeJobFamilyResponseBody as QueryRecentChangeJobFamilyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRecentChangeJobFamilyResponse(BaseResponse):
    data: QueryRecentChangeJobFamilyResponseBody | None
    def __init__(self, d=None) -> None: ...
