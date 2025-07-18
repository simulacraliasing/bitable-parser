from .create_file_version_response_body import CreateFileVersionResponseBody as CreateFileVersionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateFileVersionResponse(BaseResponse):
    data: CreateFileVersionResponseBody | None
    def __init__(self, d=None) -> None: ...
