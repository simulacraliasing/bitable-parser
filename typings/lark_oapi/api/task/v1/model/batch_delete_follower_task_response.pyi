from .batch_delete_follower_task_response_body import BatchDeleteFollowerTaskResponseBody as BatchDeleteFollowerTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchDeleteFollowerTaskResponse(BaseResponse):
    data: BatchDeleteFollowerTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
