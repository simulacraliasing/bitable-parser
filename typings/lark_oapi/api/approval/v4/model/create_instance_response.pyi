from .create_instance_response_body import CreateInstanceResponseBody as CreateInstanceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateInstanceResponse(BaseResponse):
    data: CreateInstanceResponseBody | None
    def __init__(self, d=None) -> None: ...
