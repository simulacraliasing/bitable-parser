from lark_oapi.core.construct import init as init

class SubscriptionCalendarAclResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SubscriptionCalendarAclResponseBodyBuilder: ...

class SubscriptionCalendarAclResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> SubscriptionCalendarAclResponseBody: ...
