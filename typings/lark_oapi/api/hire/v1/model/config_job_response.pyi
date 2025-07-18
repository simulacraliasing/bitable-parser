from .config_job_response_body import ConfigJobResponseBody as ConfigJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ConfigJobResponse(BaseResponse):
    data: ConfigJobResponseBody | None
    def __init__(self, d=None) -> None: ...
