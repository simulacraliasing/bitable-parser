from .batch_update_application_object_record_response_body import BatchUpdateApplicationObjectRecordResponseBody as BatchUpdateApplicationObjectRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchUpdateApplicationObjectRecordResponse(BaseResponse):
    data: BatchUpdateApplicationObjectRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
