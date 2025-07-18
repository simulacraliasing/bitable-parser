from ..model.list_job_schema_request import ListJobSchemaRequest as ListJobSchemaRequest
from ..model.list_job_schema_response import ListJobSchemaResponse as ListJobSchemaResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class JobSchema:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListJobSchemaRequest, option: RequestOption | None = None) -> ListJobSchemaResponse: ...
    async def alist(self, request: ListJobSchemaRequest, option: RequestOption | None = None) -> ListJobSchemaResponse: ...
