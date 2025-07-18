from .batch_create_app_table_record_response_body import BatchCreateAppTableRecordResponseBody as BatchCreateAppTableRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreateAppTableRecordResponse(BaseResponse):
    data: BatchCreateAppTableRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
