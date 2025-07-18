from .list_file_like_response_body import ListFileLikeResponseBody as ListFileLikeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListFileLikeResponse(BaseResponse):
    data: ListFileLikeResponseBody | None
    def __init__(self, d=None) -> None: ...
