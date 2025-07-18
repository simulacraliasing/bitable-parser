from ..model.create_space_request import CreateSpaceRequest as CreateSpaceRequest
from ..model.create_space_response import CreateSpaceResponse as CreateSpaceResponse
from ..model.get_node_space_request import GetNodeSpaceRequest as GetNodeSpaceRequest
from ..model.get_node_space_response import GetNodeSpaceResponse as GetNodeSpaceResponse
from ..model.get_space_request import GetSpaceRequest as GetSpaceRequest
from ..model.get_space_response import GetSpaceResponse as GetSpaceResponse
from ..model.list_space_request import ListSpaceRequest as ListSpaceRequest
from ..model.list_space_response import ListSpaceResponse as ListSpaceResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Space:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateSpaceRequest, option: RequestOption | None = None) -> CreateSpaceResponse: ...
    async def acreate(self, request: CreateSpaceRequest, option: RequestOption | None = None) -> CreateSpaceResponse: ...
    def get(self, request: GetSpaceRequest, option: RequestOption | None = None) -> GetSpaceResponse: ...
    async def aget(self, request: GetSpaceRequest, option: RequestOption | None = None) -> GetSpaceResponse: ...
    def get_node(self, request: GetNodeSpaceRequest, option: RequestOption | None = None) -> GetNodeSpaceResponse: ...
    async def aget_node(self, request: GetNodeSpaceRequest, option: RequestOption | None = None) -> GetNodeSpaceResponse: ...
    def list(self, request: ListSpaceRequest, option: RequestOption | None = None) -> ListSpaceResponse: ...
    async def alist(self, request: ListSpaceRequest, option: RequestOption | None = None) -> ListSpaceResponse: ...
