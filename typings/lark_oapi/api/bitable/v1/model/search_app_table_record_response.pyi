from .search_app_table_record_response_body import SearchAppTableRecordResponseBody as SearchAppTableRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchAppTableRecordResponse(BaseResponse):
    data: SearchAppTableRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
