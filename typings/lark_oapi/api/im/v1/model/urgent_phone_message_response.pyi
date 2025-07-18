from .urgent_phone_message_response_body import UrgentPhoneMessageResponseBody as UrgentPhoneMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UrgentPhoneMessageResponse(BaseResponse):
    data: UrgentPhoneMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
