from .patch_app_table_form_field_response_body import PatchAppTableFormFieldResponseBody as PatchAppTableFormFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchAppTableFormFieldResponse(BaseResponse):
    data: PatchAppTableFormFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
