from ..model.create_import_task_request import CreateImportTaskRequest as CreateImportTaskRequest
from ..model.create_import_task_response import CreateImportTaskResponse as CreateImportTaskResponse
from ..model.get_import_task_request import GetImportTaskRequest as GetImportTaskRequest
from ..model.get_import_task_response import GetImportTaskResponse as GetImportTaskResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ImportTask:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateImportTaskRequest, option: RequestOption | None = None) -> CreateImportTaskResponse: ...
    async def acreate(self, request: CreateImportTaskRequest, option: RequestOption | None = None) -> CreateImportTaskResponse: ...
    def get(self, request: GetImportTaskRequest, option: RequestOption | None = None) -> GetImportTaskResponse: ...
    async def aget(self, request: GetImportTaskRequest, option: RequestOption | None = None) -> GetImportTaskResponse: ...
