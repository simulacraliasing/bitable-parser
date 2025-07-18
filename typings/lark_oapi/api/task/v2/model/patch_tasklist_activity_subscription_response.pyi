from .patch_tasklist_activity_subscription_response_body import PatchTasklistActivitySubscriptionResponseBody as PatchTasklistActivitySubscriptionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchTasklistActivitySubscriptionResponse(BaseResponse):
    data: PatchTasklistActivitySubscriptionResponseBody | None
    def __init__(self, d=None) -> None: ...
