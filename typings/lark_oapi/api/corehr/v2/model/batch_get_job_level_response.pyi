from .batch_get_job_level_response_body import BatchGetJobLevelResponseBody as BatchGetJobLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetJobLevelResponse(BaseResponse):
    data: BatchGetJobLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
