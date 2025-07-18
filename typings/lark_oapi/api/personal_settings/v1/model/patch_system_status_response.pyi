from .patch_system_status_response_body import PatchSystemStatusResponseBody as PatchSystemStatusResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchSystemStatusResponse(BaseResponse):
    data: PatchSystemStatusResponseBody | None
    def __init__(self, d=None) -> None: ...
