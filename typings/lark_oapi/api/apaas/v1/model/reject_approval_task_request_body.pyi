from lark_oapi.core.construct import init as init

class RejectApprovalTaskRequestBody:
    user_id: str | None
    opinion: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RejectApprovalTaskRequestBodyBuilder: ...

class RejectApprovalTaskRequestBodyBuilder:
    def __init__(self) -> None: ...
    def user_id(self, user_id: str) -> RejectApprovalTaskRequestBodyBuilder: ...
    def opinion(self, opinion: str) -> RejectApprovalTaskRequestBodyBuilder: ...
    def build(self) -> RejectApprovalTaskRequestBody: ...
