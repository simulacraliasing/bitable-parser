from .get_company_response_body import GetCompanyResponseBody as GetCompanyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetCompanyResponse(BaseResponse):
    data: GetCompanyResponseBody | None
    def __init__(self, d=None) -> None: ...
