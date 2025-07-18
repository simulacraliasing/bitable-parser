from .bonus_amount import BonusAmount as BonusAmount
from .i18n import I18n as I18n
from .object_id_name import ObjectIdName as ObjectIdName
from .reward_candidate import RewardCandidate as RewardCandidate
from .reward_user import RewardUser as RewardUser
from lark_oapi.core.construct import init as init

class Reward:
    id: str | None
    referrer: RewardUser | None
    candidate: RewardCandidate | None
    referral_job: ObjectIdName | None
    reason: I18n | None
    bonus: BonusAmount | None
    create_time: str | None
    rule: ObjectIdName | None
    reward_type: int | None
    job_manager: RewardUser | None
    offer_manager: RewardUser | None
    onborad_time: str | None
    conversion_time: str | None
    confirm_user: RewardUser | None
    confirm_time: str | None
    pay_user: RewardUser | None
    pay_time: str | None
    stage: int | None
    is_import: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RewardBuilder: ...

class RewardBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> RewardBuilder: ...
    def referrer(self, referrer: RewardUser) -> RewardBuilder: ...
    def candidate(self, candidate: RewardCandidate) -> RewardBuilder: ...
    def referral_job(self, referral_job: ObjectIdName) -> RewardBuilder: ...
    def reason(self, reason: I18n) -> RewardBuilder: ...
    def bonus(self, bonus: BonusAmount) -> RewardBuilder: ...
    def create_time(self, create_time: str) -> RewardBuilder: ...
    def rule(self, rule: ObjectIdName) -> RewardBuilder: ...
    def reward_type(self, reward_type: int) -> RewardBuilder: ...
    def job_manager(self, job_manager: RewardUser) -> RewardBuilder: ...
    def offer_manager(self, offer_manager: RewardUser) -> RewardBuilder: ...
    def onborad_time(self, onborad_time: str) -> RewardBuilder: ...
    def conversion_time(self, conversion_time: str) -> RewardBuilder: ...
    def confirm_user(self, confirm_user: RewardUser) -> RewardBuilder: ...
    def confirm_time(self, confirm_time: str) -> RewardBuilder: ...
    def pay_user(self, pay_user: RewardUser) -> RewardBuilder: ...
    def pay_time(self, pay_time: str) -> RewardBuilder: ...
    def stage(self, stage: int) -> RewardBuilder: ...
    def is_import(self, is_import: bool) -> RewardBuilder: ...
    def build(self) -> Reward: ...
