from .get_by_application_referral_response_body import GetByApplicationReferralResponseBody as GetByApplicationReferralResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetByApplicationReferralResponse(BaseResponse):
    data: GetByApplicationReferralResponseBody | None
    def __init__(self, d=None) -> None: ...
