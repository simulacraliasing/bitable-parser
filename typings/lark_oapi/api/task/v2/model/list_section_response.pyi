from .list_section_response_body import ListSectionResponseBody as ListSectionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSectionResponse(BaseResponse):
    data: ListSectionResponseBody | None
    def __init__(self, d=None) -> None: ...
