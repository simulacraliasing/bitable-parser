from ..model.field_extraction_contract_request import FieldExtractionContractRequest as FieldExtractionContractRequest
from ..model.field_extraction_contract_response import FieldExtractionContractResponse as FieldExtractionContractResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class Contract:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def field_extraction(self, request: FieldExtractionContractRequest, option: RequestOption | None = None) -> FieldExtractionContractResponse: ...
    async def afield_extraction(self, request: FieldExtractionContractRequest, option: RequestOption | None = None) -> FieldExtractionContractResponse: ...
