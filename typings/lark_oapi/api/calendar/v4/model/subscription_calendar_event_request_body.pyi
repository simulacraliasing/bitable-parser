from lark_oapi.core.construct import init as init

class SubscriptionCalendarEventRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SubscriptionCalendarEventRequestBodyBuilder: ...

class SubscriptionCalendarEventRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> SubscriptionCalendarEventRequestBody: ...
