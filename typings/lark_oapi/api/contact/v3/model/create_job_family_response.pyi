from .create_job_family_response_body import CreateJobFamilyResponseBody as CreateJobFamilyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateJobFamilyResponse(BaseResponse):
    data: CreateJobFamilyResponseBody | None
    def __init__(self, d=None) -> None: ...
