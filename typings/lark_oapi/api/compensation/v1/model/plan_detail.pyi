from .i18n_content import I18nContent as I18nContent
from .plan_indicator import PlanIndicator as PlanIndicator
from .plan_item import PlanItem as PlanItem
from .plan_scope import PlanScope as PlanScope
from lark_oapi.core.construct import init as init

class PlanDetail:
    id: str | None
    tid: str | None
    name: str | None
    description: str | None
    effective_date: str | None
    plan_scope: PlanScope | None
    currency_id: str | None
    probation_salary_status: bool | None
    plan_items: list[PlanItem] | None
    plan_indicators: list[PlanIndicator] | None
    i18n_names: list[I18nContent] | None
    i18n_descriptions: list[I18nContent] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PlanDetailBuilder: ...

class PlanDetailBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> PlanDetailBuilder: ...
    def tid(self, tid: str) -> PlanDetailBuilder: ...
    def name(self, name: str) -> PlanDetailBuilder: ...
    def description(self, description: str) -> PlanDetailBuilder: ...
    def effective_date(self, effective_date: str) -> PlanDetailBuilder: ...
    def plan_scope(self, plan_scope: PlanScope) -> PlanDetailBuilder: ...
    def currency_id(self, currency_id: str) -> PlanDetailBuilder: ...
    def probation_salary_status(self, probation_salary_status: bool) -> PlanDetailBuilder: ...
    def plan_items(self, plan_items: list[PlanItem]) -> PlanDetailBuilder: ...
    def plan_indicators(self, plan_indicators: list[PlanIndicator]) -> PlanDetailBuilder: ...
    def i18n_names(self, i18n_names: list[I18nContent]) -> PlanDetailBuilder: ...
    def i18n_descriptions(self, i18n_descriptions: list[I18nContent]) -> PlanDetailBuilder: ...
    def build(self) -> PlanDetail: ...
