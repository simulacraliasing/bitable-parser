from ..model.get_role_request import GetRoleRequest as GetRoleRequest
from ..model.get_role_response import GetRoleResponse as GetRoleResponse
from ..model.list_role_request import ListRoleRequest as ListRoleRequest
from ..model.list_role_response import ListRoleResponse as ListRoleResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Role:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetRoleRequest, option: RequestOption | None = None) -> GetRoleResponse: ...
    async def aget(self, request: GetRoleRequest, option: RequestOption | None = None) -> GetRoleResponse: ...
    def list(self, request: ListRoleRequest, option: RequestOption | None = None) -> ListRoleResponse: ...
    async def alist(self, request: ListRoleRequest, option: RequestOption | None = None) -> ListRoleResponse: ...
