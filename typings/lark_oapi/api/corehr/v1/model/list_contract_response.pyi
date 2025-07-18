from .list_contract_response_body import ListContractResponseBody as ListContractResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListContractResponse(BaseResponse):
    data: ListContractResponseBody | None
    def __init__(self, d=None) -> None: ...
