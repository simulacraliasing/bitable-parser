from .update_entity_response_body import UpdateEntityResponseBody as UpdateEntityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateEntityResponse(BaseResponse):
    data: UpdateEntityResponseBody | None
    def __init__(self, d=None) -> None: ...
