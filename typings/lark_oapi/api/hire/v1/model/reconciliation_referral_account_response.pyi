from .reconciliation_referral_account_response_body import ReconciliationReferralAccountResponseBody as ReconciliationReferralAccountResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ReconciliationReferralAccountResponse(BaseResponse):
    data: ReconciliationReferralAccountResponseBody | None
    def __init__(self, d=None) -> None: ...
