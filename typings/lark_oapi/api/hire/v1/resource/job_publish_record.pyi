from ..model.search_job_publish_record_request import SearchJobPublishRecordRequest as SearchJobPublishRecordRequest
from ..model.search_job_publish_record_response import SearchJobPublishRecordResponse as SearchJobPublishRecordResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class JobPublishRecord:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def search(self, request: SearchJobPublishRecordRequest, option: RequestOption | None = None) -> SearchJobPublishRecordResponse: ...
    async def asearch(self, request: SearchJobPublishRecordRequest, option: RequestOption | None = None) -> SearchJobPublishRecordResponse: ...
