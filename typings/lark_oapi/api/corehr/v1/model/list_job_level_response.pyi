from .list_job_level_response_body import ListJobLevelResponseBody as ListJobLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobLevelResponse(BaseResponse):
    data: ListJobLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
