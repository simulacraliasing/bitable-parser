from .i18n_names import I18nNames as I18nNames
from lark_oapi.core.construct import init as init

class UserLeave:
    approval_id: str | None
    uniq_id: str | None
    unit: int | None
    interval: int | None
    start_time: str | None
    end_time: str | None
    i18n_names: I18nNames | None
    default_locale: str | None
    reason: str | None
    approve_pass_time: str | None
    approve_apply_time: str | None
    idempotent_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UserLeaveBuilder: ...

class UserLeaveBuilder:
    def __init__(self) -> None: ...
    def approval_id(self, approval_id: str) -> UserLeaveBuilder: ...
    def uniq_id(self, uniq_id: str) -> UserLeaveBuilder: ...
    def unit(self, unit: int) -> UserLeaveBuilder: ...
    def interval(self, interval: int) -> UserLeaveBuilder: ...
    def start_time(self, start_time: str) -> UserLeaveBuilder: ...
    def end_time(self, end_time: str) -> UserLeaveBuilder: ...
    def i18n_names(self, i18n_names: I18nNames) -> UserLeaveBuilder: ...
    def default_locale(self, default_locale: str) -> UserLeaveBuilder: ...
    def reason(self, reason: str) -> UserLeaveBuilder: ...
    def approve_pass_time(self, approve_pass_time: str) -> UserLeaveBuilder: ...
    def approve_apply_time(self, approve_apply_time: str) -> UserLeaveBuilder: ...
    def idempotent_id(self, idempotent_id: str) -> UserLeaveBuilder: ...
    def build(self) -> UserLeave: ...
