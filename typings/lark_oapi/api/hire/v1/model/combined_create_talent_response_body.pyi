from lark_oapi.core.construct import init as init

class CombinedCreateTalentResponseBody:
    talent_id: str | None
    creator_id: str | None
    creator_account_type: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CombinedCreateTalentResponseBodyBuilder: ...

class CombinedCreateTalentResponseBodyBuilder:
    def __init__(self) -> None: ...
    def talent_id(self, talent_id: str) -> CombinedCreateTalentResponseBodyBuilder: ...
    def creator_id(self, creator_id: str) -> CombinedCreateTalentResponseBodyBuilder: ...
    def creator_account_type(self, creator_account_type: int) -> CombinedCreateTalentResponseBodyBuilder: ...
    def build(self) -> CombinedCreateTalentResponseBody: ...
