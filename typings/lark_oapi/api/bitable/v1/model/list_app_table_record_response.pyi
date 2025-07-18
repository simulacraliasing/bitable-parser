from .list_app_table_record_response_body import ListAppTableRecordResponseBody as ListAppTableRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppTableRecordResponse(BaseResponse):
    data: ListAppTableRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
