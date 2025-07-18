from .update_job_family_response_body import UpdateJobFamilyResponseBody as UpdateJobFamilyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateJobFamilyResponse(BaseResponse):
    data: UpdateJobFamilyResponseBody | None
    def __init__(self, d=None) -> None: ...
