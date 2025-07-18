from .get_app_table_record_response_body import GetAppTableRecordResponseBody as GetAppTableRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAppTableRecordResponse(BaseResponse):
    data: GetAppTableRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
