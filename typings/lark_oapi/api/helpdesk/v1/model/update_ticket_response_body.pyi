from lark_oapi.core.construct import init as init

class UpdateTicketResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UpdateTicketResponseBodyBuilder: ...

class UpdateTicketResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> UpdateTicketResponseBody: ...
