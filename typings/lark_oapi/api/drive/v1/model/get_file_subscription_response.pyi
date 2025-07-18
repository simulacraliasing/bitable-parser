from .get_file_subscription_response_body import GetFileSubscriptionResponseBody as GetFileSubscriptionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetFileSubscriptionResponse(BaseResponse):
    data: GetFileSubscriptionResponseBody | None
    def __init__(self, d=None) -> None: ...
