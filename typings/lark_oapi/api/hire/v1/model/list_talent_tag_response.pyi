from .list_talent_tag_response_body import ListTalentTagResponseBody as ListTalentTagResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTalentTagResponse(BaseResponse):
    data: ListTalentTagResponseBody | None
    def __init__(self, d=None) -> None: ...
