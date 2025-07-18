from .copy_file_response_body import CopyFileResponseBody as CopyFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CopyFileResponse(BaseResponse):
    data: CopyFileResponseBody | None
    def __init__(self, d=None) -> None: ...
