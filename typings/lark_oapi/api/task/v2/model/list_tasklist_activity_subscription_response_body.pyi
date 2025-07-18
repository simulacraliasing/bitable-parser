from .tasklist_activity_subscription import TasklistActivitySubscription as TasklistActivitySubscription
from lark_oapi.core.construct import init as init

class ListTasklistActivitySubscriptionResponseBody:
    items: list[TasklistActivitySubscription] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListTasklistActivitySubscriptionResponseBodyBuilder: ...

class ListTasklistActivitySubscriptionResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[TasklistActivitySubscription]) -> ListTasklistActivitySubscriptionResponseBodyBuilder: ...
    def build(self) -> ListTasklistActivitySubscriptionResponseBody: ...
