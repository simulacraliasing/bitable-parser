from .list_file_version_response_body import ListFileVersionResponseBody as ListFileVersionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListFileVersionResponse(BaseResponse):
    data: ListFileVersionResponseBody | None
    def __init__(self, d=None) -> None: ...
