from .get_section_response_body import GetSectionResponseBody as GetSectionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSectionResponse(BaseResponse):
    data: GetSectionResponseBody | None
    def __init__(self, d=None) -> None: ...
