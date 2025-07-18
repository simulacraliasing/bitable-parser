from .query_authorization_response_body import QueryAuthorizationResponseBody as QueryAuthorizationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryAuthorizationResponse(BaseResponse):
    data: QueryAuthorizationResponseBody | None
    def __init__(self, d=None) -> None: ...
