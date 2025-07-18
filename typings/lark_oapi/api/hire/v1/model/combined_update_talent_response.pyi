from .combined_update_talent_response_body import CombinedUpdateTalentResponseBody as CombinedUpdateTalentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CombinedUpdateTalentResponse(BaseResponse):
    data: CombinedUpdateTalentResponseBody | None
    def __init__(self, d=None) -> None: ...
