from .create_company_response_body import CreateCompanyResponseBody as CreateCompanyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCompanyResponse(BaseResponse):
    data: CreateCompanyResponseBody | None
    def __init__(self, d=None) -> None: ...
