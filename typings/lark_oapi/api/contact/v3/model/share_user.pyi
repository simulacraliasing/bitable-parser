from .avatar_info import AvatarInfo as AvatarInfo
from lark_oapi.core.construct import init as init

class ShareUser:
    open_id: str | None
    name: str | None
    en_name: str | None
    avatar: AvatarInfo | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ShareUserBuilder: ...

class ShareUserBuilder:
    def __init__(self) -> None: ...
    def open_id(self, open_id: str) -> ShareUserBuilder: ...
    def name(self, name: str) -> ShareUserBuilder: ...
    def en_name(self, en_name: str) -> ShareUserBuilder: ...
    def avatar(self, avatar: AvatarInfo) -> ShareUserBuilder: ...
    def build(self) -> ShareUser: ...
