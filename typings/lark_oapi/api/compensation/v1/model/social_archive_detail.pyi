from .i18n import I18n as I18n
from .social_archive_item import SocialArchiveItem as SocialArchiveItem
from lark_oapi.core.construct import init as init

class SocialArchiveDetail:
    description: I18n | None
    insurance_type: str | None
    insurance_status: str | None
    id: str | None
    tid: str | None
    plan_id: str | None
    plan_tid: str | None
    location_id: str | None
    company_id: str | None
    account_type: str | None
    insurance_account: str | None
    base_salary: str | None
    insurance_details: list[SocialArchiveItem] | None
    effective_date: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SocialArchiveDetailBuilder: ...

class SocialArchiveDetailBuilder:
    def __init__(self) -> None: ...
    def description(self, description: I18n) -> SocialArchiveDetailBuilder: ...
    def insurance_type(self, insurance_type: str) -> SocialArchiveDetailBuilder: ...
    def insurance_status(self, insurance_status: str) -> SocialArchiveDetailBuilder: ...
    def id(self, id: str) -> SocialArchiveDetailBuilder: ...
    def tid(self, tid: str) -> SocialArchiveDetailBuilder: ...
    def plan_id(self, plan_id: str) -> SocialArchiveDetailBuilder: ...
    def plan_tid(self, plan_tid: str) -> SocialArchiveDetailBuilder: ...
    def location_id(self, location_id: str) -> SocialArchiveDetailBuilder: ...
    def company_id(self, company_id: str) -> SocialArchiveDetailBuilder: ...
    def account_type(self, account_type: str) -> SocialArchiveDetailBuilder: ...
    def insurance_account(self, insurance_account: str) -> SocialArchiveDetailBuilder: ...
    def base_salary(self, base_salary: str) -> SocialArchiveDetailBuilder: ...
    def insurance_details(self, insurance_details: list[SocialArchiveItem]) -> SocialArchiveDetailBuilder: ...
    def effective_date(self, effective_date: str) -> SocialArchiveDetailBuilder: ...
    def build(self) -> SocialArchiveDetail: ...
