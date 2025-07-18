from .batch_query_external_interview_response_body import BatchQueryExternalInterviewResponseBody as BatchQueryExternalInterviewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchQueryExternalInterviewResponse(BaseResponse):
    data: BatchQueryExternalInterviewResponseBody | None
    def __init__(self, d=None) -> None: ...
