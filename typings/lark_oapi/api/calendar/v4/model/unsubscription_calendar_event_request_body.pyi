from lark_oapi.core.construct import init as init

class UnsubscriptionCalendarEventRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UnsubscriptionCalendarEventRequestBodyBuilder: ...

class UnsubscriptionCalendarEventRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> UnsubscriptionCalendarEventRequestBody: ...
