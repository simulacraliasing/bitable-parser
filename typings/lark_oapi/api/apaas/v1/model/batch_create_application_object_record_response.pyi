from .batch_create_application_object_record_response_body import BatchCreateApplicationObjectRecordResponseBody as BatchCreateApplicationObjectRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreateApplicationObjectRecordResponse(BaseResponse):
    data: BatchCreateApplicationObjectRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
