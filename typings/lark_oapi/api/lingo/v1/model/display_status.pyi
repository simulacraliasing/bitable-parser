from lark_oapi.core.construct import init as init

class DisplayStatus:
    allow_highlight: bool | None
    allow_search: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DisplayStatusBuilder: ...

class DisplayStatusBuilder:
    def __init__(self) -> None: ...
    def allow_highlight(self, allow_highlight: bool) -> DisplayStatusBuilder: ...
    def allow_search(self, allow_search: bool) -> DisplayStatusBuilder: ...
    def build(self) -> DisplayStatus: ...
