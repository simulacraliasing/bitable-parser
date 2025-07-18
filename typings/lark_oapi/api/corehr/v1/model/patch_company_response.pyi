from .patch_company_response_body import PatchCompanyResponseBody as PatchCompanyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchCompanyResponse(BaseResponse):
    data: PatchCompanyResponseBody | None
    def __init__(self, d=None) -> None: ...
