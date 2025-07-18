from .create_exam_response_body import CreateExamResponseBody as CreateExamResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExamResponse(BaseResponse):
    data: CreateExamResponseBody | None
    def __init__(self, d=None) -> None: ...
