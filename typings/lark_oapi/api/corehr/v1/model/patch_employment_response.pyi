from .patch_employment_response_body import PatchEmploymentResponseBody as PatchEmploymentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchEmploymentResponse(BaseResponse):
    data: PatchEmploymentResponseBody | None
    def __init__(self, d=None) -> None: ...
