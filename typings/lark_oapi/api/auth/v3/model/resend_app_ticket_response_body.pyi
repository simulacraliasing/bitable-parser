from lark_oapi.core.construct import init as init

class ResendAppTicketResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ResendAppTicketResponseBodyBuilder: ...

class ResendAppTicketResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ResendAppTicketResponseBody: ...
