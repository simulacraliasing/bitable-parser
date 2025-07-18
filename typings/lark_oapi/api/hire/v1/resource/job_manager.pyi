from ..model.batch_update_job_manager_request import BatchUpdateJobManagerRequest as BatchUpdateJobManagerRequest
from ..model.batch_update_job_manager_response import BatchUpdateJobManagerResponse as BatchUpdateJobManagerResponse
from ..model.get_job_manager_request import GetJobManagerRequest as GetJobManagerRequest
from ..model.get_job_manager_response import GetJobManagerResponse as GetJobManagerResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class JobManager:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_update(self, request: BatchUpdateJobManagerRequest, option: RequestOption | None = None) -> BatchUpdateJobManagerResponse: ...
    async def abatch_update(self, request: BatchUpdateJobManagerRequest, option: RequestOption | None = None) -> BatchUpdateJobManagerResponse: ...
    def get(self, request: GetJobManagerRequest, option: RequestOption | None = None) -> GetJobManagerResponse: ...
    async def aget(self, request: GetJobManagerRequest, option: RequestOption | None = None) -> GetJobManagerResponse: ...
