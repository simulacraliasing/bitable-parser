from .create_tasklist_activity_subscription_response_body import CreateTasklistActivitySubscriptionResponseBody as CreateTasklistActivitySubscriptionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTasklistActivitySubscriptionResponse(BaseResponse):
    data: CreateTasklistActivitySubscriptionResponseBody | None
    def __init__(self, d=None) -> None: ...
