from .patch_job_response_body import PatchJobResponseBody as PatchJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchJobResponse(BaseResponse):
    data: PatchJobResponseBody | None
    def __init__(self, d=None) -> None: ...
