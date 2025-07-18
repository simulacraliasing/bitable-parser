from .batch_get_id_talent_response_body import BatchGetIdTalentResponseBody as BatchGetIdTalentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetIdTalentResponse(BaseResponse):
    data: BatchGetIdTalentResponseBody | None
    def __init__(self, d=None) -> None: ...
