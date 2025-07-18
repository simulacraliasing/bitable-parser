from .list_job_function_response_body import ListJobFunctionResponseBody as ListJobFunctionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobFunctionResponse(BaseResponse):
    data: ListJobFunctionResponseBody | None
    def __init__(self, d=None) -> None: ...
