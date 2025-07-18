from .list_talent_response_body import ListTalentResponseBody as ListTalentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTalentResponse(BaseResponse):
    data: ListTalentResponseBody | None
    def __init__(self, d=None) -> None: ...
