from .batch_get_id_user_response_body import BatchGetIdUserResponseBody as BatchGetIdUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetIdUserResponse(BaseResponse):
    data: BatchGetIdUserResponseBody | None
    def __init__(self, d=None) -> None: ...
