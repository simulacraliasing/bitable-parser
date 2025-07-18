from .search_contract_response_body import SearchContractResponseBody as SearchContractResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchContractResponse(BaseResponse):
    data: SearchContractResponseBody | None
    def __init__(self, d=None) -> None: ...
