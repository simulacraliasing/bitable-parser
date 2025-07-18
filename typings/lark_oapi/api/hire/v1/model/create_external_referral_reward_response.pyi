from .create_external_referral_reward_response_body import CreateExternalReferralRewardResponseBody as CreateExternalReferralRewardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExternalReferralRewardResponse(BaseResponse):
    data: CreateExternalReferralRewardResponseBody | None
    def __init__(self, d=None) -> None: ...
