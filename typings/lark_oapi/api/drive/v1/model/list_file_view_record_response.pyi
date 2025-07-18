from .list_file_view_record_response_body import ListFileViewRecordResponseBody as ListFileViewRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListFileViewRecordResponse(BaseResponse):
    data: ListFileViewRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
