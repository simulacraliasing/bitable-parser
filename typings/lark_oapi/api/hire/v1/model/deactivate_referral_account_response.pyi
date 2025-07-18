from .deactivate_referral_account_response_body import DeactivateReferralAccountResponseBody as DeactivateReferralAccountResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeactivateReferralAccountResponse(BaseResponse):
    data: DeactivateReferralAccountResponseBody | None
    def __init__(self, d=None) -> None: ...
