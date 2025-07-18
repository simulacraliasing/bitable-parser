from .list_resume_source_response_body import ListResumeSourceResponseBody as ListResumeSourceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListResumeSourceResponse(BaseResponse):
    data: ListResumeSourceResponseBody | None
    def __init__(self, d=None) -> None: ...
