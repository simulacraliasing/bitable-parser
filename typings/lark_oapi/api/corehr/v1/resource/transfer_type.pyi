from ..model.query_transfer_type_request import QueryTransferTypeRequest as QueryTransferTypeRequest
from ..model.query_transfer_type_response import QueryTransferTypeResponse as QueryTransferTypeResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class TransferType:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def query(self, request: QueryTransferTypeRequest, option: RequestOption | None = None) -> QueryTransferTypeResponse: ...
    async def aquery(self, request: QueryTransferTypeRequest, option: RequestOption | None = None) -> QueryTransferTypeResponse: ...
