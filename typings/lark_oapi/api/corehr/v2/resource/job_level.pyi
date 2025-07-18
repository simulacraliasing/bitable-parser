from ..model.batch_get_job_level_request import BatchGetJobLevelRequest as BatchGetJobLevelRequest
from ..model.batch_get_job_level_response import BatchGetJobLevelResponse as BatchGetJobLevelResponse
from ..model.query_recent_change_job_level_request import QueryRecentChangeJobLevelRequest as QueryRecentChangeJobLevelRequest
from ..model.query_recent_change_job_level_response import QueryRecentChangeJobLevelResponse as QueryRecentChangeJobLevelResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class JobLevel:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_get(self, request: BatchGetJobLevelRequest, option: RequestOption | None = None) -> BatchGetJobLevelResponse: ...
    async def abatch_get(self, request: BatchGetJobLevelRequest, option: RequestOption | None = None) -> BatchGetJobLevelResponse: ...
    def query_recent_change(self, request: QueryRecentChangeJobLevelRequest, option: RequestOption | None = None) -> QueryRecentChangeJobLevelResponse: ...
    async def aquery_recent_change(self, request: QueryRecentChangeJobLevelRequest, option: RequestOption | None = None) -> QueryRecentChangeJobLevelResponse: ...
