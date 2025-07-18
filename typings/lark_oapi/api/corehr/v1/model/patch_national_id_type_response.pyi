from .patch_national_id_type_response_body import PatchNationalIdTypeResponseBody as PatchNationalIdTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchNationalIdTypeResponse(BaseResponse):
    data: PatchNationalIdTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
