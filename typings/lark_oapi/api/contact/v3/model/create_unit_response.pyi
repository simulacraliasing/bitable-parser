from .create_unit_response_body import CreateUnitResponseBody as CreateUnitResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateUnitResponse(BaseResponse):
    data: CreateUnitResponseBody | None
    def __init__(self, d=None) -> None: ...
