from .batch_update_app_table_record_response_body import BatchUpdateAppTableRecordResponseBody as BatchUpdateAppTableRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchUpdateAppTableRecordResponse(BaseResponse):
    data: BatchUpdateAppTableRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
