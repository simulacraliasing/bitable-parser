from .enable_referral_account_response_body import EnableReferralAccountResponseBody as EnableReferralAccountResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class EnableReferralAccountResponse(BaseResponse):
    data: EnableReferralAccountResponseBody | None
    def __init__(self, d=None) -> None: ...
