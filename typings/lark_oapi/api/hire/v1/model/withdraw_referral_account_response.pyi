from .withdraw_referral_account_response_body import WithdrawReferralAccountResponseBody as WithdrawReferralAccountResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class WithdrawReferralAccountResponse(BaseResponse):
    data: WithdrawReferralAccountResponseBody | None
    def __init__(self, d=None) -> None: ...
