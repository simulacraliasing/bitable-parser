from .preview_instance_response_body import PreviewInstanceResponseBody as PreviewInstanceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PreviewInstanceResponse(BaseResponse):
    data: PreviewInstanceResponseBody | None
    def __init__(self, d=None) -> None: ...
