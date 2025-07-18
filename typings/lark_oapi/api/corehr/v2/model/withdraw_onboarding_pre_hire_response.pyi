from .withdraw_onboarding_pre_hire_response_body import WithdrawOnboardingPreHireResponseBody as WithdrawOnboardingPreHireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class WithdrawOnboardingPreHireResponse(BaseResponse):
    data: WithdrawOnboardingPreHireResponseBody | None
    def __init__(self, d=None) -> None: ...
