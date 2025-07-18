from .grant import Grant as Grant
from lark_oapi.core.construct import init as init

class CreateBadgeGrantResponseBody:
    grant: Grant | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateBadgeGrantResponseBodyBuilder: ...

class CreateBadgeGrantResponseBodyBuilder:
    def __init__(self) -> None: ...
    def grant(self, grant: Grant) -> CreateBadgeGrantResponseBodyBuilder: ...
    def build(self) -> CreateBadgeGrantResponseBody: ...
