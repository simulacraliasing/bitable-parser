from ..model.query_user_task_request import QueryUserTaskRequest as QueryUserTaskRequest
from ..model.query_user_task_response import QueryUserTaskResponse as QueryUserTaskResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class UserTask:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def query(self, request: QueryUserTaskRequest, option: RequestOption | None = None) -> QueryUserTaskResponse: ...
    async def aquery(self, request: QueryUserTaskRequest, option: RequestOption | None = None) -> QueryUserTaskResponse: ...
