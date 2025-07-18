from ..model.create_user_approval_request import CreateUserApprovalRequest as CreateUserApprovalRequest
from ..model.create_user_approval_response import CreateUserApprovalResponse as CreateUserApprovalResponse
from ..model.query_user_approval_request import QueryUserApprovalRequest as QueryUserApprovalRequest
from ..model.query_user_approval_response import QueryUserApprovalResponse as QueryUserApprovalResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class UserApproval:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateUserApprovalRequest, option: RequestOption | None = None) -> CreateUserApprovalResponse: ...
    async def acreate(self, request: CreateUserApprovalRequest, option: RequestOption | None = None) -> CreateUserApprovalResponse: ...
    def query(self, request: QueryUserApprovalRequest, option: RequestOption | None = None) -> QueryUserApprovalResponse: ...
    async def aquery(self, request: QueryUserApprovalRequest, option: RequestOption | None = None) -> QueryUserApprovalResponse: ...
