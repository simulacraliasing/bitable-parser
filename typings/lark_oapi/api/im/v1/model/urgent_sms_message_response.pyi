from .urgent_sms_message_response_body import UrgentSmsMessageResponseBody as UrgentSmsMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UrgentSmsMessageResponse(BaseResponse):
    data: UrgentSmsMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
