from .patch_job_level_response_body import PatchJobLevelResponseBody as PatchJobLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchJobLevelResponse(BaseResponse):
    data: PatchJobLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
