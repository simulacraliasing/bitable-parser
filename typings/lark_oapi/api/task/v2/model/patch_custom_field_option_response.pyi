from .patch_custom_field_option_response_body import PatchCustomFieldOptionResponseBody as PatchCustomFieldOptionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchCustomFieldOptionResponse(BaseResponse):
    data: PatchCustomFieldOptionResponseBody | None
    def __init__(self, d=None) -> None: ...
