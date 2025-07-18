from .batch_get_okr_response_body import BatchGetOkrResponseBody as BatchGetOkrResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetOkrResponse(BaseResponse):
    data: BatchGetOkrResponseBody | None
    def __init__(self, d=None) -> None: ...
