from .id_with_name import IdWithName as IdWithName
from .verif_plan_snapshot import VerifPlanSnapshot as VerifPlanSnapshot
from lark_oapi.core.construct import init as init

class VerificationActivity:
    activity_id: str | None
    plan_id: str | None
    version_id: str | None
    name: IdWithName | None
    activity_status: int | None
    pay_period_seq: str | None
    retro_period_seq: str | None
    plan_snapshot: VerifPlanSnapshot | None
    update_time: int | None
    approve_time: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> VerificationActivityBuilder: ...

class VerificationActivityBuilder:
    def __init__(self) -> None: ...
    def activity_id(self, activity_id: str) -> VerificationActivityBuilder: ...
    def plan_id(self, plan_id: str) -> VerificationActivityBuilder: ...
    def version_id(self, version_id: str) -> VerificationActivityBuilder: ...
    def name(self, name: IdWithName) -> VerificationActivityBuilder: ...
    def activity_status(self, activity_status: int) -> VerificationActivityBuilder: ...
    def pay_period_seq(self, pay_period_seq: str) -> VerificationActivityBuilder: ...
    def retro_period_seq(self, retro_period_seq: str) -> VerificationActivityBuilder: ...
    def plan_snapshot(self, plan_snapshot: VerifPlanSnapshot) -> VerificationActivityBuilder: ...
    def update_time(self, update_time: int) -> VerificationActivityBuilder: ...
    def approve_time(self, approve_time: int) -> VerificationActivityBuilder: ...
    def build(self) -> VerificationActivity: ...
