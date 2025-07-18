from .get_data_source_response_body import GetDataSourceResponseBody as GetDataSourceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetDataSourceResponse(BaseResponse):
    data: GetDataSourceResponseBody | None
    def __init__(self, d=None) -> None: ...
