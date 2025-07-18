from .copy_app_response_body import CopyAppResponseBody as CopyAppResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CopyAppResponse(BaseResponse):
    data: CopyAppResponseBody | None
    def __init__(self, d=None) -> None: ...
