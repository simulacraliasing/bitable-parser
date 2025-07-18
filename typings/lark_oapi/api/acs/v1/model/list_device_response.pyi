from .list_device_response_body import ListDeviceResponseBody as ListDeviceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListDeviceResponse(BaseResponse):
    data: ListDeviceResponseBody | None
    def __init__(self, d=None) -> None: ...
