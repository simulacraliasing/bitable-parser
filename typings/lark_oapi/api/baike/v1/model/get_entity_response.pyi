from .get_entity_response_body import GetEntityResponseBody as GetEntityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetEntityResponse(BaseResponse):
    data: GetEntityResponseBody | None
    def __init__(self, d=None) -> None: ...
