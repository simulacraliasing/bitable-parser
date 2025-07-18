from .get_job_level_response_body import GetJobLevelResponseBody as GetJobLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetJobLevelResponse(BaseResponse):
    data: GetJobLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
