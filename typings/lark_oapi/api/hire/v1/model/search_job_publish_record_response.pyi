from .search_job_publish_record_response_body import SearchJobPublishRecordResponseBody as SearchJobPublishRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchJobPublishRecordResponse(BaseResponse):
    data: SearchJobPublishRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
