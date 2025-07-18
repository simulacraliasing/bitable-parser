from .message import Message as Message
from lark_oapi.core.construct import init as init

class MessageWithOperation:
    message: Message | None
    operation_type: str | None
    operation_id: int | None
    intent_id: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MessageWithOperationBuilder: ...

class MessageWithOperationBuilder:
    def __init__(self) -> None: ...
    def message(self, message: Message) -> MessageWithOperationBuilder: ...
    def operation_type(self, operation_type: str) -> MessageWithOperationBuilder: ...
    def operation_id(self, operation_id: int) -> MessageWithOperationBuilder: ...
    def intent_id(self, intent_id: int) -> MessageWithOperationBuilder: ...
    def build(self) -> MessageWithOperation: ...
