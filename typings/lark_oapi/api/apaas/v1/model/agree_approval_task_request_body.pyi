from lark_oapi.core.construct import init as init

class AgreeApprovalTaskRequestBody:
    user_id: str | None
    opinion: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AgreeApprovalTaskRequestBodyBuilder: ...

class AgreeApprovalTaskRequestBodyBuilder:
    def __init__(self) -> None: ...
    def user_id(self, user_id: str) -> AgreeApprovalTaskRequestBodyBuilder: ...
    def opinion(self, opinion: str) -> AgreeApprovalTaskRequestBodyBuilder: ...
    def build(self) -> AgreeApprovalTaskRequestBody: ...
