from .agency_account import AgencyAccount as AgencyAccount
from lark_oapi.core.construct import init as init

class GetAgencyAccountAgencyResponseBody:
    has_more: bool | None
    page_token: str | None
    items: list[AgencyAccount] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetAgencyAccountAgencyResponseBodyBuilder: ...

class GetAgencyAccountAgencyResponseBodyBuilder:
    def __init__(self) -> None: ...
    def has_more(self, has_more: bool) -> GetAgencyAccountAgencyResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> GetAgencyAccountAgencyResponseBodyBuilder: ...
    def items(self, items: list[AgencyAccount]) -> GetAgencyAccountAgencyResponseBodyBuilder: ...
    def build(self) -> GetAgencyAccountAgencyResponseBody: ...
