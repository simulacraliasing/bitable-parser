from .failed_reason import FailedReason as FailedReason
from lark_oapi.core.construct import init as init

class UpdateChatButtonResponseBody:
    failed_user_reasons: list[FailedReason] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UpdateChatButtonResponseBodyBuilder: ...

class UpdateChatButtonResponseBodyBuilder:
    def __init__(self) -> None: ...
    def failed_user_reasons(self, failed_user_reasons: list[FailedReason]) -> UpdateChatButtonResponseBodyBuilder: ...
    def build(self) -> UpdateChatButtonResponseBody: ...
