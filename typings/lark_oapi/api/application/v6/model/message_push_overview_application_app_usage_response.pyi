from .message_push_overview_application_app_usage_response_body import MessagePushOverviewApplicationAppUsageResponseBody as MessagePushOverviewApplicationAppUsageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MessagePushOverviewApplicationAppUsageResponse(BaseResponse):
    data: MessagePushOverviewApplicationAppUsageResponseBody | None
    def __init__(self, d=None) -> None: ...
