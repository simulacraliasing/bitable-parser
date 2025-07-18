from .combined_create_talent_response_body import CombinedCreateTalentResponseBody as CombinedCreateTalentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CombinedCreateTalentResponse(BaseResponse):
    data: CombinedCreateTalentResponseBody | None
    def __init__(self, d=None) -> None: ...
