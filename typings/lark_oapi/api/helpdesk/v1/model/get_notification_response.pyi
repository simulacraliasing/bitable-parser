from .get_notification_response_body import GetNotificationResponseBody as GetNotificationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetNotificationResponse(BaseResponse):
    data: GetNotificationResponseBody | None
    def __init__(self, d=None) -> None: ...
