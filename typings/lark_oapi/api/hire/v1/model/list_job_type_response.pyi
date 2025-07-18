from .list_job_type_response_body import ListJobTypeResponseBody as ListJobTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobTypeResponse(BaseResponse):
    data: ListJobTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
