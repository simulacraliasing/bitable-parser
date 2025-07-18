from .create_referral_account_response_body import CreateReferralAccountResponseBody as CreateReferralAccountResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateReferralAccountResponse(BaseResponse):
    data: CreateReferralAccountResponseBody | None
    def __init__(self, d=None) -> None: ...
