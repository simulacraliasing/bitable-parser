from ..model.create_user_task_remedy_request import CreateUserTaskRemedyRequest as CreateUserTaskRemedyRequest
from ..model.create_user_task_remedy_response import CreateUserTaskRemedyResponse as CreateUserTaskRemedyResponse
from ..model.query_user_allowed_remedys_user_task_remedy_request import QueryUserAllowedRemedysUserTaskRemedyRequest as QueryUserAllowedRemedysUserTaskRemedyRequest
from ..model.query_user_allowed_remedys_user_task_remedy_response import QueryUserAllowedRemedysUserTaskRemedyResponse as QueryUserAllowedRemedysUserTaskRemedyResponse
from ..model.query_user_task_remedy_request import QueryUserTaskRemedyRequest as QueryUserTaskRemedyRequest
from ..model.query_user_task_remedy_response import QueryUserTaskRemedyResponse as QueryUserTaskRemedyResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class UserTaskRemedy:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateUserTaskRemedyRequest, option: RequestOption | None = None) -> CreateUserTaskRemedyResponse: ...
    async def acreate(self, request: CreateUserTaskRemedyRequest, option: RequestOption | None = None) -> CreateUserTaskRemedyResponse: ...
    def query(self, request: QueryUserTaskRemedyRequest, option: RequestOption | None = None) -> QueryUserTaskRemedyResponse: ...
    async def aquery(self, request: QueryUserTaskRemedyRequest, option: RequestOption | None = None) -> QueryUserTaskRemedyResponse: ...
    def query_user_allowed_remedys(self, request: QueryUserAllowedRemedysUserTaskRemedyRequest, option: RequestOption | None = None) -> QueryUserAllowedRemedysUserTaskRemedyResponse: ...
    async def aquery_user_allowed_remedys(self, request: QueryUserAllowedRemedysUserTaskRemedyRequest, option: RequestOption | None = None) -> QueryUserAllowedRemedysUserTaskRemedyResponse: ...
