from ..model.get_job_title_request import GetJobTitleRequest as GetJobTitleRequest
from ..model.get_job_title_response import GetJobTitleResponse as GetJobTitleResponse
from ..model.list_job_title_request import ListJobTitleRequest as ListJobTitleRequest
from ..model.list_job_title_response import ListJobTitleResponse as ListJobTitleResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class JobTitle:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetJobTitleRequest, option: RequestOption | None = None) -> GetJobTitleResponse: ...
    async def aget(self, request: GetJobTitleRequest, option: RequestOption | None = None) -> GetJobTitleResponse: ...
    def list(self, request: ListJobTitleRequest, option: RequestOption | None = None) -> ListJobTitleResponse: ...
    async def alist(self, request: ListJobTitleRequest, option: RequestOption | None = None) -> ListJobTitleResponse: ...
