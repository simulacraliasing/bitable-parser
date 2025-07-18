from .list_company_response_body import ListCompanyResponseBody as ListCompanyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCompanyResponse(BaseResponse):
    data: ListCompanyResponseBody | None
    def __init__(self, d=None) -> None: ...
