from ..model.list_job_function_request import ListJobFunctionRequest as ListJobFunctionRequest
from ..model.list_job_function_response import ListJobFunctionResponse as ListJobFunctionResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class JobFunction:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListJobFunctionRequest, option: RequestOption | None = None) -> ListJobFunctionResponse: ...
    async def alist(self, request: ListJobFunctionRequest, option: RequestOption | None = None) -> ListJobFunctionResponse: ...
