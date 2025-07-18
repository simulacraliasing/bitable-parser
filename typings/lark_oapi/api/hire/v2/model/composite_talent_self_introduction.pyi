from .talent_customized_data_child import TalentCustomizedDataChild as TalentCustomizedDataChild
from lark_oapi.core.construct import init as init

class CompositeTalentSelfIntroduction:
    self_introduction: str | None
    customized_data_list: list[TalentCustomizedDataChild] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CompositeTalentSelfIntroductionBuilder: ...

class CompositeTalentSelfIntroductionBuilder:
    def __init__(self) -> None: ...
    def self_introduction(self, self_introduction: str) -> CompositeTalentSelfIntroductionBuilder: ...
    def customized_data_list(self, customized_data_list: list[TalentCustomizedDataChild]) -> CompositeTalentSelfIntroductionBuilder: ...
    def build(self) -> CompositeTalentSelfIntroduction: ...
