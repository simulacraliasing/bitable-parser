from .batch_get_job_family_response_body import BatchGetJobFamilyResponseBody as BatchGetJobFamilyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetJobFamilyResponse(BaseResponse):
    data: BatchGetJobFamilyResponseBody | None
    def __init__(self, d=None) -> None: ...
