from .create_entity_response_body import CreateEntityResponseBody as CreateEntityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateEntityResponse(BaseResponse):
    data: CreateEntityResponseBody | None
    def __init__(self, d=None) -> None: ...
