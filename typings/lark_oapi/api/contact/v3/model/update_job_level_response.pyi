from .update_job_level_response_body import UpdateJobLevelResponseBody as UpdateJobLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateJobLevelResponse(BaseResponse):
    data: UpdateJobLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
