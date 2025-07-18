from .batch_update_job_manager_response_body import BatchUpdateJobManagerResponseBody as BatchUpdateJobManagerResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchUpdateJobManagerResponse(BaseResponse):
    data: BatchUpdateJobManagerResponseBody | None
    def __init__(self, d=None) -> None: ...
