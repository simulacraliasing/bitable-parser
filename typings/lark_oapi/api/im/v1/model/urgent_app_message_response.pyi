from .urgent_app_message_response_body import UrgentAppMessageResponseBody as UrgentAppMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UrgentAppMessageResponse(BaseResponse):
    data: UrgentAppMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
