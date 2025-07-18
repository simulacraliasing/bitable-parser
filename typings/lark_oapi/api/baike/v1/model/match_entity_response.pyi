from .match_entity_response_body import MatchEntityResponseBody as MatchEntityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MatchEntityResponse(BaseResponse):
    data: MatchEntityResponseBody | None
    def __init__(self, d=None) -> None: ...
