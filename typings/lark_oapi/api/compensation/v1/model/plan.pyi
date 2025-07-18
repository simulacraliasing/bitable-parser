from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class Plan:
    plan_id: str | None
    plan_tid: str | None
    name: I18n | None
    people_id: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PlanBuilder: ...

class PlanBuilder:
    def __init__(self) -> None: ...
    def plan_id(self, plan_id: str) -> PlanBuilder: ...
    def plan_tid(self, plan_tid: str) -> PlanBuilder: ...
    def name(self, name: I18n) -> PlanBuilder: ...
    def people_id(self, people_id: int) -> PlanBuilder: ...
    def build(self) -> Plan: ...
