from .combined_update_job_response_body import CombinedUpdateJobResponseBody as CombinedUpdateJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CombinedUpdateJobResponse(BaseResponse):
    data: CombinedUpdateJobResponseBody | None
    def __init__(self, d=None) -> None: ...
