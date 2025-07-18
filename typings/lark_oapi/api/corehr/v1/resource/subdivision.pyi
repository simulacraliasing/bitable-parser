from ..model.get_subdivision_request import GetSubdivisionRequest as GetSubdivisionRequest
from ..model.get_subdivision_response import GetSubdivisionResponse as GetSubdivisionResponse
from ..model.list_subdivision_request import ListSubdivisionRequest as ListSubdivisionRequest
from ..model.list_subdivision_response import ListSubdivisionResponse as ListSubdivisionResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Subdivision:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetSubdivisionRequest, option: RequestOption | None = None) -> GetSubdivisionResponse: ...
    async def aget(self, request: GetSubdivisionRequest, option: RequestOption | None = None) -> GetSubdivisionResponse: ...
    def list(self, request: ListSubdivisionRequest, option: RequestOption | None = None) -> ListSubdivisionResponse: ...
    async def alist(self, request: ListSubdivisionRequest, option: RequestOption | None = None) -> ListSubdivisionResponse: ...
