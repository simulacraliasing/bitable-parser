from lark_oapi.core.construct import init as init

class RecruitmentType:
    id: str | None
    name: str | None
    en_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RecruitmentTypeBuilder: ...

class RecruitmentTypeBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> RecruitmentTypeBuilder: ...
    def name(self, name: str) -> RecruitmentTypeBuilder: ...
    def en_name(self, en_name: str) -> RecruitmentTypeBuilder: ...
    def build(self) -> RecruitmentType: ...
