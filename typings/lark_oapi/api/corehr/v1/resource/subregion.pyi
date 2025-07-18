from ..model.get_subregion_request import GetSubregionRequest as GetSubregionRequest
from ..model.get_subregion_response import GetSubregionResponse as GetSubregionResponse
from ..model.list_subregion_request import ListSubregionRequest as ListSubregionRequest
from ..model.list_subregion_response import ListSubregionResponse as ListSubregionResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Subregion:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetSubregionRequest, option: RequestOption | None = None) -> GetSubregionResponse: ...
    async def aget(self, request: GetSubregionRequest, option: RequestOption | None = None) -> GetSubregionResponse: ...
    def list(self, request: ListSubregionRequest, option: RequestOption | None = None) -> ListSubregionResponse: ...
    async def alist(self, request: ListSubregionRequest, option: RequestOption | None = None) -> ListSubregionResponse: ...
