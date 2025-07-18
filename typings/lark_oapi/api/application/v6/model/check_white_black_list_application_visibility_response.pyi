from .check_white_black_list_application_visibility_response_body import CheckWhiteBlackListApplicationVisibilityResponseBody as CheckWhiteBlackListApplicationVisibilityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CheckWhiteBlackListApplicationVisibilityResponse(BaseResponse):
    data: CheckWhiteBlackListApplicationVisibilityResponseBody | None
    def __init__(self, d=None) -> None: ...
