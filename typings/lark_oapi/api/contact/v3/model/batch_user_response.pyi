from .batch_user_response_body import BatchUserResponseBody as BatchUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchUserResponse(BaseResponse):
    data: BatchUserResponseBody | None
    def __init__(self, d=None) -> None: ...
