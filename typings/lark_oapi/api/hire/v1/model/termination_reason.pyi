from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class TerminationReason:
    id: str | None
    name: I18n | None
    referral_name: I18n | None
    termination_type: int | None
    is_used_as_evaluation: bool | None
    active_status: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TerminationReasonBuilder: ...

class TerminationReasonBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> TerminationReasonBuilder: ...
    def name(self, name: I18n) -> TerminationReasonBuilder: ...
    def referral_name(self, referral_name: I18n) -> TerminationReasonBuilder: ...
    def termination_type(self, termination_type: int) -> TerminationReasonBuilder: ...
    def is_used_as_evaluation(self, is_used_as_evaluation: bool) -> TerminationReasonBuilder: ...
    def active_status(self, active_status: int) -> TerminationReasonBuilder: ...
    def build(self) -> TerminationReason: ...
