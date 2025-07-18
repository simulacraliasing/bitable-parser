from .talent_customized_data_child import TalentCustomizedDataChild as TalentCustomizedDataChild
from lark_oapi.core.construct import init as init

class CompositeTalentCareerInfo:
    company_name: str | None
    description: str | None
    end_time: str | None
    start_time: str | None
    title: str | None
    customized_data_list: list[TalentCustomizedDataChild] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CompositeTalentCareerInfoBuilder: ...

class CompositeTalentCareerInfoBuilder:
    def __init__(self) -> None: ...
    def company_name(self, company_name: str) -> CompositeTalentCareerInfoBuilder: ...
    def description(self, description: str) -> CompositeTalentCareerInfoBuilder: ...
    def end_time(self, end_time: str) -> CompositeTalentCareerInfoBuilder: ...
    def start_time(self, start_time: str) -> CompositeTalentCareerInfoBuilder: ...
    def title(self, title: str) -> CompositeTalentCareerInfoBuilder: ...
    def customized_data_list(self, customized_data_list: list[TalentCustomizedDataChild]) -> CompositeTalentCareerInfoBuilder: ...
    def build(self) -> CompositeTalentCareerInfo: ...
