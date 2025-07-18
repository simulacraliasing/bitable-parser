from .create_contract_response_body import CreateContractResponseBody as CreateContractResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateContractResponse(BaseResponse):
    data: CreateContractResponseBody | None
    def __init__(self, d=None) -> None: ...
