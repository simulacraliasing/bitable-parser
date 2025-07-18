from .get_tasklist_activity_subscription_response_body import GetTasklistActivitySubscriptionResponseBody as GetTasklistActivitySubscriptionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetTasklistActivitySubscriptionResponse(BaseResponse):
    data: GetTasklistActivitySubscriptionResponseBody | None
    def __init__(self, d=None) -> None: ...
