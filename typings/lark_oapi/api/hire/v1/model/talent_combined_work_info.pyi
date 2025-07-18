from .talent_customized_data_object_value import TalentCustomizedDataObjectValue as TalentCustomizedDataObjectValue
from lark_oapi.core.construct import init as init

class TalentCombinedWorkInfo:
    id: str | None
    link: str | None
    desc: str | None
    attachment_id: str | None
    customized_data: list[TalentCustomizedDataObjectValue] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TalentCombinedWorkInfoBuilder: ...

class TalentCombinedWorkInfoBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> TalentCombinedWorkInfoBuilder: ...
    def link(self, link: str) -> TalentCombinedWorkInfoBuilder: ...
    def desc(self, desc: str) -> TalentCombinedWorkInfoBuilder: ...
    def attachment_id(self, attachment_id: str) -> TalentCombinedWorkInfoBuilder: ...
    def customized_data(self, customized_data: list[TalentCustomizedDataObjectValue]) -> TalentCombinedWorkInfoBuilder: ...
    def build(self) -> TalentCombinedWorkInfo: ...
