from .create_task_follower_response_body import CreateTaskFollowerResponseBody as CreateTaskFollowerResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTaskFollowerResponse(BaseResponse):
    data: CreateTaskFollowerResponseBody | None
    def __init__(self, d=None) -> None: ...
