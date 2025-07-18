from .abnormal_reason_element import AbnormalReasonElement as AbnormalReasonElement
from lark_oapi.core.construct import init as init

class AbnormalReasonI18nElement:
    lang: str | None
    elements: list[AbnormalReasonElement] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AbnormalReasonI18nElementBuilder: ...

class AbnormalReasonI18nElementBuilder:
    def __init__(self) -> None: ...
    def lang(self, lang: str) -> AbnormalReasonI18nElementBuilder: ...
    def elements(self, elements: list[AbnormalReasonElement]) -> AbnormalReasonI18nElementBuilder: ...
    def build(self) -> AbnormalReasonI18nElement: ...
