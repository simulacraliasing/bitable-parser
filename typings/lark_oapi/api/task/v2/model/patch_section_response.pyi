from .patch_section_response_body import PatchSectionResponseBody as PatchSectionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchSectionResponse(BaseResponse):
    data: PatchSectionResponseBody | None
    def __init__(self, d=None) -> None: ...
