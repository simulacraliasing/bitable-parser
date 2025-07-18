from .get_app_response_body import GetAppResponseBody as GetAppResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAppResponse(BaseResponse):
    data: GetAppResponseBody | None
    def __init__(self, d=None) -> None: ...
