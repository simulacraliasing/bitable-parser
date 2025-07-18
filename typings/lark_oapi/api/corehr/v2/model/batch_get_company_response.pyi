from .batch_get_company_response_body import BatchGetCompanyResponseBody as BatchGetCompanyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetCompanyResponse(BaseResponse):
    data: BatchGetCompanyResponseBody | None
    def __init__(self, d=None) -> None: ...
