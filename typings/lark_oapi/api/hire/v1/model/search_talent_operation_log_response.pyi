from .search_talent_operation_log_response_body import SearchTalentOperationLogResponseBody as SearchTalentOperationLogResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchTalentOperationLogResponse(BaseResponse):
    data: SearchTalentOperationLogResponseBody | None
    def __init__(self, d=None) -> None: ...
