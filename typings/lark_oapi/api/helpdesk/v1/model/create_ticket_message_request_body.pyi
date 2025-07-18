from lark_oapi.core.construct import init as init

class CreateTicketMessageRequestBody:
    msg_type: str | None
    content: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateTicketMessageRequestBodyBuilder: ...

class CreateTicketMessageRequestBodyBuilder:
    def __init__(self) -> None: ...
    def msg_type(self, msg_type: str) -> CreateTicketMessageRequestBodyBuilder: ...
    def content(self, content: str) -> CreateTicketMessageRequestBodyBuilder: ...
    def build(self) -> CreateTicketMessageRequestBody: ...
