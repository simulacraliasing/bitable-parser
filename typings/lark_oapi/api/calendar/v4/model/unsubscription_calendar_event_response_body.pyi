from lark_oapi.core.construct import init as init

class UnsubscriptionCalendarEventResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UnsubscriptionCalendarEventResponseBodyBuilder: ...

class UnsubscriptionCalendarEventResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> UnsubscriptionCalendarEventResponseBody: ...
