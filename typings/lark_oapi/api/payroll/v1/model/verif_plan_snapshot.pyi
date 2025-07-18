from .id_with_name import IdWithName as IdWithName
from .verif_data_source_rule import VerifDataSourceRule as VerifDataSourceRule
from .verif_filter_rule import VerifFilterRule as VerifFilterRule
from .verif_item import VerifItem as VerifItem
from .verif_pay_calendar import VerifPayCalendar as VerifPayCalendar
from lark_oapi.core.construct import init as init

class VerifPlanSnapshot:
    is_retro: bool | None
    is_collect: bool | None
    is_proration: bool | None
    country_region: IdWithName | None
    currency: IdWithName | None
    calendar_type: int | None
    pay_calendars: list[VerifPayCalendar] | None
    scope_type: int | None
    pay_groups: list[IdWithName] | None
    filter_type: int | None
    filter_rule: VerifFilterRule | None
    approval_type: int | None
    items: list[VerifItem] | None
    data_source_rule: VerifDataSourceRule | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> VerifPlanSnapshotBuilder: ...

class VerifPlanSnapshotBuilder:
    def __init__(self) -> None: ...
    def is_retro(self, is_retro: bool) -> VerifPlanSnapshotBuilder: ...
    def is_collect(self, is_collect: bool) -> VerifPlanSnapshotBuilder: ...
    def is_proration(self, is_proration: bool) -> VerifPlanSnapshotBuilder: ...
    def country_region(self, country_region: IdWithName) -> VerifPlanSnapshotBuilder: ...
    def currency(self, currency: IdWithName) -> VerifPlanSnapshotBuilder: ...
    def calendar_type(self, calendar_type: int) -> VerifPlanSnapshotBuilder: ...
    def pay_calendars(self, pay_calendars: list[VerifPayCalendar]) -> VerifPlanSnapshotBuilder: ...
    def scope_type(self, scope_type: int) -> VerifPlanSnapshotBuilder: ...
    def pay_groups(self, pay_groups: list[IdWithName]) -> VerifPlanSnapshotBuilder: ...
    def filter_type(self, filter_type: int) -> VerifPlanSnapshotBuilder: ...
    def filter_rule(self, filter_rule: VerifFilterRule) -> VerifPlanSnapshotBuilder: ...
    def approval_type(self, approval_type: int) -> VerifPlanSnapshotBuilder: ...
    def items(self, items: list[VerifItem]) -> VerifPlanSnapshotBuilder: ...
    def data_source_rule(self, data_source_rule: VerifDataSourceRule) -> VerifPlanSnapshotBuilder: ...
    def build(self) -> VerifPlanSnapshot: ...
