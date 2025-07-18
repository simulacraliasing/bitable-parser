from .get_moto_response_body import GetMotoResponseBody as GetMotoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMotoResponse(BaseResponse):
    data: GetMotoResponseBody | None
    def __init__(self, d=None) -> None: ...
