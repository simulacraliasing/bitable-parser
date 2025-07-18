from .list_tasklist_activity_subscription_response_body import ListTasklistActivitySubscriptionResponseBody as ListTasklistActivitySubscriptionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTasklistActivitySubscriptionResponse(BaseResponse):
    data: ListTasklistActivitySubscriptionResponseBody | None
    def __init__(self, d=None) -> None: ...
