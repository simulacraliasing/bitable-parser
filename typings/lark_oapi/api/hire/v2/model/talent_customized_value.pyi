from .talent_customized_attachment import TalentCustomizedAttachment as TalentCustomizedAttachment
from .talent_customized_option import TalentCustomizedOption as TalentCustomizedOption
from .talent_customized_time_range import TalentCustomizedTimeRange as TalentCustomizedTimeRange
from lark_oapi.core.construct import init as init

class TalentCustomizedValue:
    content: str | None
    option: TalentCustomizedOption | None
    option_list: list[TalentCustomizedOption] | None
    time_range: TalentCustomizedTimeRange | None
    time: str | None
    number: str | None
    customized_attachment: list[TalentCustomizedAttachment] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TalentCustomizedValueBuilder: ...

class TalentCustomizedValueBuilder:
    def __init__(self) -> None: ...
    def content(self, content: str) -> TalentCustomizedValueBuilder: ...
    def option(self, option: TalentCustomizedOption) -> TalentCustomizedValueBuilder: ...
    def option_list(self, option_list: list[TalentCustomizedOption]) -> TalentCustomizedValueBuilder: ...
    def time_range(self, time_range: TalentCustomizedTimeRange) -> TalentCustomizedValueBuilder: ...
    def time(self, time: str) -> TalentCustomizedValueBuilder: ...
    def number(self, number: str) -> TalentCustomizedValueBuilder: ...
    def customized_attachment(self, customized_attachment: list[TalentCustomizedAttachment]) -> TalentCustomizedValueBuilder: ...
    def build(self) -> TalentCustomizedValue: ...
