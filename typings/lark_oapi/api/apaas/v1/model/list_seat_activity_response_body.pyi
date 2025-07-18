from .seat_activity import SeatActivity as SeatActivity
from lark_oapi.core.construct import init as init

class ListSeatActivityResponseBody:
    items: list[SeatActivity] | None
    page_token: str | None
    has_more: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListSeatActivityResponseBodyBuilder: ...

class ListSeatActivityResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[SeatActivity]) -> ListSeatActivityResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> ListSeatActivityResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> ListSeatActivityResponseBodyBuilder: ...
    def build(self) -> ListSeatActivityResponseBody: ...
