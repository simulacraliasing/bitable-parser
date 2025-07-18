from lark_oapi.core.construct import init as init

class TalentBatchInfo:
    talent_id: str | None
    mobile_code: str | None
    mobile_number: str | None
    email: str | None
    identification_type: int | None
    identification_number: str | None
    is_onboarded: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TalentBatchInfoBuilder: ...

class TalentBatchInfoBuilder:
    def __init__(self) -> None: ...
    def talent_id(self, talent_id: str) -> TalentBatchInfoBuilder: ...
    def mobile_code(self, mobile_code: str) -> TalentBatchInfoBuilder: ...
    def mobile_number(self, mobile_number: str) -> TalentBatchInfoBuilder: ...
    def email(self, email: str) -> TalentBatchInfoBuilder: ...
    def identification_type(self, identification_type: int) -> TalentBatchInfoBuilder: ...
    def identification_number(self, identification_number: str) -> TalentBatchInfoBuilder: ...
    def is_onboarded(self, is_onboarded: bool) -> TalentBatchInfoBuilder: ...
    def build(self) -> TalentBatchInfo: ...
