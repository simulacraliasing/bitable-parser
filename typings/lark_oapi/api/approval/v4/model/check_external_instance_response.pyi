from .check_external_instance_response_body import CheckExternalInstanceResponseBody as CheckExternalInstanceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CheckExternalInstanceResponse(BaseResponse):
    data: CheckExternalInstanceResponseBody | None
    def __init__(self, d=None) -> None: ...
