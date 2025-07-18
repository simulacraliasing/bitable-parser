from .get_contract_response_body import GetContractResponseBody as GetContractResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetContractResponse(BaseResponse):
    data: GetContractResponseBody | None
    def __init__(self, d=None) -> None: ...
