from .query_talent_object_response_body import QueryTalentObjectResponseBody as QueryTalentObjectResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryTalentObjectResponse(BaseResponse):
    data: QueryTalentObjectResponseBody | None
    def __init__(self, d=None) -> None: ...
