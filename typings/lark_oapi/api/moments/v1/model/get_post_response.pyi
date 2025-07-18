from .get_post_response_body import GetPostResponseBody as GetPostResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetPostResponse(BaseResponse):
    data: GetPostResponseBody | None
    def __init__(self, d=None) -> None: ...
