from lark_oapi.core.construct import init as init

class Email:
    id: str | None
    title: str | None
    owner_type: int | None
    create_time: int | None
    owner_user_id: str | None
    owner_address: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EmailBuilder: ...

class EmailBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> EmailBuilder: ...
    def title(self, title: str) -> EmailBuilder: ...
    def owner_type(self, owner_type: int) -> EmailBuilder: ...
    def create_time(self, create_time: int) -> EmailBuilder: ...
    def owner_user_id(self, owner_user_id: str) -> EmailBuilder: ...
    def owner_address(self, owner_address: str) -> EmailBuilder: ...
    def build(self) -> Email: ...
