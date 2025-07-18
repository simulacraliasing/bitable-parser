from ..model.create_task_subtask_request import CreateTaskSubtaskRequest as CreateTaskSubtaskRequest
from ..model.create_task_subtask_response import CreateTaskSubtaskResponse as CreateTaskSubtaskResponse
from ..model.list_task_subtask_request import ListTaskSubtaskRequest as ListTaskSubtaskRequest
from ..model.list_task_subtask_response import ListTaskSubtaskResponse as ListTaskSubtaskResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class TaskSubtask:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateTaskSubtaskRequest, option: RequestOption | None = None) -> CreateTaskSubtaskResponse: ...
    async def acreate(self, request: CreateTaskSubtaskRequest, option: RequestOption | None = None) -> CreateTaskSubtaskResponse: ...
    def list(self, request: ListTaskSubtaskRequest, option: RequestOption | None = None) -> ListTaskSubtaskResponse: ...
    async def alist(self, request: ListTaskSubtaskRequest, option: RequestOption | None = None) -> ListTaskSubtaskResponse: ...
