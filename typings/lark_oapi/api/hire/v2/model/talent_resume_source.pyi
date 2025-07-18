from lark_oapi.core.construct import init as init

class TalentResumeSource:
    id: str | None
    zh_name: str | None
    en_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TalentResumeSourceBuilder: ...

class TalentResumeSourceBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> TalentResumeSourceBuilder: ...
    def zh_name(self, zh_name: str) -> TalentResumeSourceBuilder: ...
    def en_name(self, en_name: str) -> TalentResumeSourceBuilder: ...
    def build(self) -> TalentResumeSource: ...
