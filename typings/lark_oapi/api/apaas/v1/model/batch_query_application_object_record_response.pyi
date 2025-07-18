from .batch_query_application_object_record_response_body import BatchQueryApplicationObjectRecordResponseBody as BatchQueryApplicationObjectRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchQueryApplicationObjectRecordResponse(BaseResponse):
    data: BatchQueryApplicationObjectRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
