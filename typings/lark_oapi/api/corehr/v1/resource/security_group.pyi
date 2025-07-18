from ..model.list_security_group_request import ListSecurityGroupRequest as ListSecurityGroupRequest
from ..model.list_security_group_response import ListSecurityGroupResponse as ListSecurityGroupResponse
from ..model.query_security_group_request import QuerySecurityGroupRequest as QuerySecurityGroupRequest
from ..model.query_security_group_response import QuerySecurityGroupResponse as QuerySecurityGroupResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class SecurityGroup:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListSecurityGroupRequest, option: RequestOption | None = None) -> ListSecurityGroupResponse: ...
    async def alist(self, request: ListSecurityGroupRequest, option: RequestOption | None = None) -> ListSecurityGroupResponse: ...
    def query(self, request: QuerySecurityGroupRequest, option: RequestOption | None = None) -> QuerySecurityGroupResponse: ...
    async def aquery(self, request: QuerySecurityGroupRequest, option: RequestOption | None = None) -> QuerySecurityGroupResponse: ...
