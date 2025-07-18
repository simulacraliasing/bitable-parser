from ..model.update_process_transfer_request import UpdateProcessTransferRequest as UpdateProcessTransferRequest
from ..model.update_process_transfer_response import UpdateProcessTransferResponse as UpdateProcessTransferResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ProcessTransfer:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def update(self, request: UpdateProcessTransferRequest, option: RequestOption | None = None) -> UpdateProcessTransferResponse: ...
    async def aupdate(self, request: UpdateProcessTransferRequest, option: RequestOption | None = None) -> UpdateProcessTransferResponse: ...
