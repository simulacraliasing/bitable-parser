from .patch_file_subscription_response_body import PatchFileSubscriptionResponseBody as PatchFileSubscriptionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchFileSubscriptionResponse(BaseResponse):
    data: PatchFileSubscriptionResponseBody | None
    def __init__(self, d=None) -> None: ...
