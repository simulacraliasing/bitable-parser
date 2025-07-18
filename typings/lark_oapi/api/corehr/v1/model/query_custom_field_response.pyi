from .query_custom_field_response_body import QueryCustomFieldResponseBody as QueryCustomFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryCustomFieldResponse(BaseResponse):
    data: QueryCustomFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
