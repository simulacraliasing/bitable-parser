from .create_file_response_body import CreateFileResponseBody as CreateFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateFileResponse(BaseResponse):
    data: CreateFileResponseBody | None
    def __init__(self, d=None) -> None: ...
