from .get_instance_response_body import GetInstanceResponseBody as GetInstanceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetInstanceResponse(BaseResponse):
    data: GetInstanceResponseBody | None
    def __init__(self, d=None) -> None: ...
