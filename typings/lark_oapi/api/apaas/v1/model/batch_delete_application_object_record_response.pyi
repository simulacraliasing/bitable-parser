from .batch_delete_application_object_record_response_body import BatchDeleteApplicationObjectRecordResponseBody as BatchDeleteApplicationObjectRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchDeleteApplicationObjectRecordResponse(BaseResponse):
    data: BatchDeleteApplicationObjectRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
