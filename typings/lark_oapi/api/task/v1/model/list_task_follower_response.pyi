from .list_task_follower_response_body import ListTaskFollowerResponseBody as ListTaskFollowerResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTaskFollowerResponse(BaseResponse):
    data: ListTaskFollowerResponseBody | None
    def __init__(self, d=None) -> None: ...
