from .create_moto_response_body import CreateMotoResponseBody as CreateMotoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateMotoResponse(BaseResponse):
    data: CreateMotoResponseBody | None
    def __init__(self, d=None) -> None: ...
