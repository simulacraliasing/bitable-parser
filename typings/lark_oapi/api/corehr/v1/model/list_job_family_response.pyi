from .list_job_family_response_body import ListJobFamilyResponseBody as ListJobFamilyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobFamilyResponse(BaseResponse):
    data: ListJobFamilyResponseBody | None
    def __init__(self, d=None) -> None: ...
