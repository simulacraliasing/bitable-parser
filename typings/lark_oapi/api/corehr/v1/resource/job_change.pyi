from ..model.create_job_change_request import CreateJobChangeRequest as CreateJobChangeRequest
from ..model.create_job_change_response import CreateJobChangeResponse as CreateJobChangeResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class JobChange:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateJobChangeRequest, option: RequestOption | None = None) -> CreateJobChangeResponse: ...
    async def acreate(self, request: CreateJobChangeRequest, option: RequestOption | None = None) -> CreateJobChangeResponse: ...
