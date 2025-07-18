from .get_content_response_body import GetContentResponseBody as GetContentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetContentResponse(BaseResponse):
    data: GetContentResponseBody | None
    def __init__(self, d=None) -> None: ...
