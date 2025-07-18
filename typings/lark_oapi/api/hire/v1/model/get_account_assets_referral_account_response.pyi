from .get_account_assets_referral_account_response_body import GetAccountAssetsReferralAccountResponseBody as GetAccountAssetsReferralAccountResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAccountAssetsReferralAccountResponse(BaseResponse):
    data: GetAccountAssetsReferralAccountResponseBody | None
    def __init__(self, d=None) -> None: ...
