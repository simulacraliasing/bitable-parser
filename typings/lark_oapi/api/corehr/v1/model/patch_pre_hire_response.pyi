from .patch_pre_hire_response_body import PatchPreHireResponseBody as PatchPreHireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchPreHireResponse(BaseResponse):
    data: PatchPreHireResponseBody | None
    def __init__(self, d=None) -> None: ...
