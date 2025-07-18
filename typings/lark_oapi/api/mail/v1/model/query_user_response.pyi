from .query_user_response_body import QueryUserResponseBody as QueryUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserResponse(BaseResponse):
    data: QueryUserResponseBody | None
    def __init__(self, d=None) -> None: ...
