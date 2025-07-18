from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class Sentence:
    content: str | None
    speak_time: str | None
    user_type: int | None
    speaker_name: I18n | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SentenceBuilder: ...

class SentenceBuilder:
    def __init__(self) -> None: ...
    def content(self, content: str) -> SentenceBuilder: ...
    def speak_time(self, speak_time: str) -> SentenceBuilder: ...
    def user_type(self, user_type: int) -> SentenceBuilder: ...
    def speaker_name(self, speaker_name: I18n) -> SentenceBuilder: ...
    def build(self) -> Sentence: ...
