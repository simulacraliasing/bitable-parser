from .patch_app_table_form_response_body import PatchAppTableFormResponseBody as PatchAppTableFormResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchAppTableFormResponse(BaseResponse):
    data: PatchAppTableFormResponseBody | None
    def __init__(self, d=None) -> None: ...
