from .create_job_level_response_body import CreateJobLevelResponseBody as CreateJobLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateJobLevelResponse(BaseResponse):
    data: CreateJobLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
