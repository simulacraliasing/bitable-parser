from ..model.get_process_request import GetProcessRequest as GetProcessRequest
from ..model.get_process_response import GetProcessResponse as GetProcessResponse
from ..model.list_process_request import ListProcessRequest as ListProcessRequest
from ..model.list_process_response import ListProcessResponse as ListProcessResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Process:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetProcessRequest, option: RequestOption | None = None) -> GetProcessResponse: ...
    async def aget(self, request: GetProcessRequest, option: RequestOption | None = None) -> GetProcessResponse: ...
    def list(self, request: ListProcessRequest, option: RequestOption | None = None) -> ListProcessResponse: ...
    async def alist(self, request: ListProcessRequest, option: RequestOption | None = None) -> ListProcessResponse: ...
