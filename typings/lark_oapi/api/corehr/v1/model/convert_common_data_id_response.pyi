from .convert_common_data_id_response_body import ConvertCommonDataIdResponseBody as ConvertCommonDataIdResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ConvertCommonDataIdResponse(BaseResponse):
    data: ConvertCommonDataIdResponseBody | None
    def __init__(self, d=None) -> None: ...
