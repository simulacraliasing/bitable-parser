from .patch_custom_field_response_body import PatchCustomFieldResponseBody as PatchCustomFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchCustomFieldResponse(BaseResponse):
    data: PatchCustomFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
