from .search_referral_response_body import SearchReferralResponseBody as SearchReferralResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchReferralResponse(BaseResponse):
    data: SearchReferralResponseBody | None
    def __init__(self, d=None) -> None: ...
