from .field_extraction_contract_response_body import FieldExtractionContractResponseBody as FieldExtractionContractResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class FieldExtractionContractResponse(BaseResponse):
    data: FieldExtractionContractResponseBody | None
    def __init__(self, d=None) -> None: ...
