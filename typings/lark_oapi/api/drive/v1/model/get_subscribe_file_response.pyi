from .get_subscribe_file_response_body import GetSubscribeFileResponseBody as GetSubscribeFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSubscribeFileResponse(BaseResponse):
    data: GetSubscribeFileResponseBody | None
    def __init__(self, d=None) -> None: ...
