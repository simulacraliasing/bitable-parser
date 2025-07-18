from lark_oapi.core.construct import init as init

class ProcessApprovalInfoRequestBody:
    approval_id: str | None
    approval_type: str | None
    status: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ProcessApprovalInfoRequestBodyBuilder: ...

class ProcessApprovalInfoRequestBodyBuilder:
    def __init__(self) -> None: ...
    def approval_id(self, approval_id: str) -> ProcessApprovalInfoRequestBodyBuilder: ...
    def approval_type(self, approval_type: str) -> ProcessApprovalInfoRequestBodyBuilder: ...
    def status(self, status: int) -> ProcessApprovalInfoRequestBodyBuilder: ...
    def build(self) -> ProcessApprovalInfoRequestBody: ...
