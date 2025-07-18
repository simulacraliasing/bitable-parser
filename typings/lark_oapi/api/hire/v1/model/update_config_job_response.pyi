from .update_config_job_response_body import UpdateConfigJobResponseBody as UpdateConfigJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateConfigJobResponse(BaseResponse):
    data: UpdateConfigJobResponseBody | None
    def __init__(self, d=None) -> None: ...
