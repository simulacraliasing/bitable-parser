from .patch_job_family_response_body import PatchJobFamilyResponseBody as PatchJobFamilyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchJobFamilyResponse(BaseResponse):
    data: PatchJobFamilyResponseBody | None
    def __init__(self, d=None) -> None: ...
