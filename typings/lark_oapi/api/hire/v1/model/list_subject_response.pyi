from .list_subject_response_body import ListSubjectResponseBody as ListSubjectResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSubjectResponse(BaseResponse):
    data: ListSubjectResponseBody | None
    def __init__(self, d=None) -> None: ...
