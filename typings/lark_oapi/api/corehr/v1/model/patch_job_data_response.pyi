from .patch_job_data_response_body import PatchJobDataResponseBody as PatchJobDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchJobDataResponse(BaseResponse):
    data: PatchJobDataResponseBody | None
    def __init__(self, d=None) -> None: ...
