from .leave_time import LeaveTime as LeaveTime
from lark_oapi.core.construct import init as init

class LeaveRequestCreated:
    employment_id: str | None
    leave_type_id: str | None
    start_time: LeaveTime | None
    end_time: LeaveTime | None
    time_zone: str | None
    daily_leave_mode: str | None
    arrive_late_minutes: int | None
    leave_early_minutes: int | None
    notes: str | None
    date_of_marriage_certificate: str | None
    provide_premarital_examination_materials: bool | None
    is_couple_live_apart: bool | None
    difficulty_giving_birth: bool | None
    pregnant_months: int | None
    due_date: str | None
    child_date_of_birth: str | None
    number_of_newborns: int | None
    applicable_scenarios: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> LeaveRequestCreatedBuilder: ...

class LeaveRequestCreatedBuilder:
    def __init__(self) -> None: ...
    def employment_id(self, employment_id: str) -> LeaveRequestCreatedBuilder: ...
    def leave_type_id(self, leave_type_id: str) -> LeaveRequestCreatedBuilder: ...
    def start_time(self, start_time: LeaveTime) -> LeaveRequestCreatedBuilder: ...
    def end_time(self, end_time: LeaveTime) -> LeaveRequestCreatedBuilder: ...
    def time_zone(self, time_zone: str) -> LeaveRequestCreatedBuilder: ...
    def daily_leave_mode(self, daily_leave_mode: str) -> LeaveRequestCreatedBuilder: ...
    def arrive_late_minutes(self, arrive_late_minutes: int) -> LeaveRequestCreatedBuilder: ...
    def leave_early_minutes(self, leave_early_minutes: int) -> LeaveRequestCreatedBuilder: ...
    def notes(self, notes: str) -> LeaveRequestCreatedBuilder: ...
    def date_of_marriage_certificate(self, date_of_marriage_certificate: str) -> LeaveRequestCreatedBuilder: ...
    def provide_premarital_examination_materials(self, provide_premarital_examination_materials: bool) -> LeaveRequestCreatedBuilder: ...
    def is_couple_live_apart(self, is_couple_live_apart: bool) -> LeaveRequestCreatedBuilder: ...
    def difficulty_giving_birth(self, difficulty_giving_birth: bool) -> LeaveRequestCreatedBuilder: ...
    def pregnant_months(self, pregnant_months: int) -> LeaveRequestCreatedBuilder: ...
    def due_date(self, due_date: str) -> LeaveRequestCreatedBuilder: ...
    def child_date_of_birth(self, child_date_of_birth: str) -> LeaveRequestCreatedBuilder: ...
    def number_of_newborns(self, number_of_newborns: int) -> LeaveRequestCreatedBuilder: ...
    def applicable_scenarios(self, applicable_scenarios: str) -> LeaveRequestCreatedBuilder: ...
    def build(self) -> LeaveRequestCreated: ...
