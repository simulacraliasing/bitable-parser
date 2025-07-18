from .create_notification_response_body import CreateNotificationResponseBody as CreateNotificationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateNotificationResponse(BaseResponse):
    data: CreateNotificationResponseBody | None
    def __init__(self, d=None) -> None: ...
