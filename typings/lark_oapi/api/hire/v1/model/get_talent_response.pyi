from .get_talent_response_body import GetTalentResponseBody as GetTalentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetTalentResponse(BaseResponse):
    data: GetTalentResponseBody | None
    def __init__(self, d=None) -> None: ...
