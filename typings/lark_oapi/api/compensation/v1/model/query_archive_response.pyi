from .query_archive_response_body import QueryArchiveResponseBody as QueryArchiveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryArchiveResponse(BaseResponse):
    data: QueryArchiveResponseBody | None
    def __init__(self, d=None) -> None: ...
