from .referral_basic_info import ReferralBasicInfo as ReferralBasicInfo
from .referral_recommend_info import ReferralRecommendInfo as ReferralRecommendInfo
from lark_oapi.core.construct import init as init

class ReferralInfoV2:
    basic_info: ReferralBasicInfo | None
    recommend_info: ReferralRecommendInfo | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ReferralInfoV2Builder: ...

class ReferralInfoV2Builder:
    def __init__(self) -> None: ...
    def basic_info(self, basic_info: ReferralBasicInfo) -> ReferralInfoV2Builder: ...
    def recommend_info(self, recommend_info: ReferralRecommendInfo) -> ReferralInfoV2Builder: ...
    def build(self) -> ReferralInfoV2: ...
