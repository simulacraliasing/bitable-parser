from .list_entity_response_body import ListEntityResponseBody as ListEntityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListEntityResponse(BaseResponse):
    data: ListEntityResponseBody | None
    def __init__(self, d=None) -> None: ...
