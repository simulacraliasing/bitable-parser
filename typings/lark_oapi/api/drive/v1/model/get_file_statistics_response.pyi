from .get_file_statistics_response_body import GetFileStatisticsResponseBody as GetFileStatisticsResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetFileStatisticsResponse(BaseResponse):
    data: GetFileStatisticsResponseBody | None
    def __init__(self, d=None) -> None: ...
