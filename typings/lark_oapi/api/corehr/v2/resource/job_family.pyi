from ..model.batch_get_job_family_request import BatchGetJobFamilyRequest as BatchGetJobFamilyRequest
from ..model.batch_get_job_family_response import BatchGetJobFamilyResponse as BatchGetJobFamilyResponse
from ..model.query_recent_change_job_family_request import QueryRecentChangeJobFamilyRequest as QueryRecentChangeJobFamilyRequest
from ..model.query_recent_change_job_family_response import QueryRecentChangeJobFamilyResponse as QueryRecentChangeJobFamilyResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class JobFamily:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_get(self, request: BatchGetJobFamilyRequest, option: RequestOption | None = None) -> BatchGetJobFamilyResponse: ...
    async def abatch_get(self, request: BatchGetJobFamilyRequest, option: RequestOption | None = None) -> BatchGetJobFamilyResponse: ...
    def query_recent_change(self, request: QueryRecentChangeJobFamilyRequest, option: RequestOption | None = None) -> QueryRecentChangeJobFamilyResponse: ...
    async def aquery_recent_change(self, request: QueryRecentChangeJobFamilyRequest, option: RequestOption | None = None) -> QueryRecentChangeJobFamilyResponse: ...
