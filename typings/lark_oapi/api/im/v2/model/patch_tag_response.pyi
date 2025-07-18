from .patch_tag_response_body import PatchTagResponseBody as PatchTagResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchTagResponse(BaseResponse):
    data: PatchTagResponseBody | None
    def __init__(self, d=None) -> None: ...
