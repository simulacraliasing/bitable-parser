from .move_talent_talent_pool_response_body import MoveTalentTalentPoolResponseBody as MoveTalentTalentPoolResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MoveTalentTalentPoolResponse(BaseResponse):
    data: MoveTalentTalentPoolResponseBody | None
    def __init__(self, d=None) -> None: ...
