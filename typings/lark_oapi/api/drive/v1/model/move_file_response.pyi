from .move_file_response_body import MoveFileResponseBody as MoveFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MoveFileResponse(BaseResponse):
    data: MoveFileResponseBody | None
    def __init__(self, d=None) -> None: ...
