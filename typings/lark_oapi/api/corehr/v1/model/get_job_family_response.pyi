from .get_job_family_response_body import GetJobFamilyResponseBody as GetJobFamilyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetJobFamilyResponse(BaseResponse):
    data: GetJobFamilyResponseBody | None
    def __init__(self, d=None) -> None: ...
