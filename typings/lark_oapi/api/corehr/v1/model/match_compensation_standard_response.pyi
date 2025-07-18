from .match_compensation_standard_response_body import MatchCompensationStandardResponseBody as MatchCompensationStandardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MatchCompensationStandardResponse(BaseResponse):
    data: MatchCompensationStandardResponseBody | None
    def __init__(self, d=None) -> None: ...
