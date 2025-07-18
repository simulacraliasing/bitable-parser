from .get_file_version_response_body import GetFileVersionResponseBody as GetFileVersionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetFileVersionResponse(BaseResponse):
    data: GetFileVersionResponseBody | None
    def __init__(self, d=None) -> None: ...
