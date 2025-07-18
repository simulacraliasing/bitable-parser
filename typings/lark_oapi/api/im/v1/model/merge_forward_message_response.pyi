from .merge_forward_message_response_body import MergeForwardMessageResponseBody as MergeForwardMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MergeForwardMessageResponse(BaseResponse):
    data: MergeForwardMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
