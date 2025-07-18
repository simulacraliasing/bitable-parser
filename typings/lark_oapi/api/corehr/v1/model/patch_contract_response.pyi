from .patch_contract_response_body import PatchContractResponseBody as PatchContractResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchContractResponse(BaseResponse):
    data: PatchContractResponseBody | None
    def __init__(self, d=None) -> None: ...
