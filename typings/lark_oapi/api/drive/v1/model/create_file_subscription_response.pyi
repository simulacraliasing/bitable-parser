from .create_file_subscription_response_body import CreateFileSubscriptionResponseBody as CreateFileSubscriptionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateFileSubscriptionResponse(BaseResponse):
    data: CreateFileSubscriptionResponseBody | None
    def __init__(self, d=None) -> None: ...
