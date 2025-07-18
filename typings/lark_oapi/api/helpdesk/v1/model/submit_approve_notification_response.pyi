from .submit_approve_notification_response_body import SubmitApproveNotificationResponseBody as SubmitApproveNotificationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SubmitApproveNotificationResponse(BaseResponse):
    data: SubmitApproveNotificationResponseBody | None
    def __init__(self, d=None) -> None: ...
