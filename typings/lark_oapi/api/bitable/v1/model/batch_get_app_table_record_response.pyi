from .batch_get_app_table_record_response_body import BatchGetAppTableRecordResponseBody as BatchGetAppTableRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetAppTableRecordResponse(BaseResponse):
    data: BatchGetAppTableRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
