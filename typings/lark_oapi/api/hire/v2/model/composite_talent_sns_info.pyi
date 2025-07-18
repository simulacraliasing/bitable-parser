from .talent_customized_data_child import TalentCustomizedDataChild as TalentCustomizedDataChild
from lark_oapi.core.construct import init as init

class CompositeTalentSnsInfo:
    sns_type: int | None
    link: str | None
    customized_data_list: list[TalentCustomizedDataChild] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CompositeTalentSnsInfoBuilder: ...

class CompositeTalentSnsInfoBuilder:
    def __init__(self) -> None: ...
    def sns_type(self, sns_type: int) -> CompositeTalentSnsInfoBuilder: ...
    def link(self, link: str) -> CompositeTalentSnsInfoBuilder: ...
    def customized_data_list(self, customized_data_list: list[TalentCustomizedDataChild]) -> CompositeTalentSnsInfoBuilder: ...
    def build(self) -> CompositeTalentSnsInfo: ...
