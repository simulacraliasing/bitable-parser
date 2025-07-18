from .batch_delete_app_table_record_response_body import BatchDeleteAppTableRecordResponseBody as BatchDeleteAppTableRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchDeleteAppTableRecordResponse(BaseResponse):
    data: BatchDeleteAppTableRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
