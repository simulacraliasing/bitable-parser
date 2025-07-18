from lark_oapi.core.construct import init as init

class Version:
    name: str | None
    version: str | None
    parent_token: str | None
    owner_id: str | None
    creator_id: str | None
    create_time: int | None
    update_time: int | None
    status: int | None
    obj_type: str | None
    parent_type: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> VersionBuilder: ...

class VersionBuilder:
    def __init__(self) -> None: ...
    def name(self, name: str) -> VersionBuilder: ...
    def version(self, version: str) -> VersionBuilder: ...
    def parent_token(self, parent_token: str) -> VersionBuilder: ...
    def owner_id(self, owner_id: str) -> VersionBuilder: ...
    def creator_id(self, creator_id: str) -> VersionBuilder: ...
    def create_time(self, create_time: int) -> VersionBuilder: ...
    def update_time(self, update_time: int) -> VersionBuilder: ...
    def status(self, status: int) -> VersionBuilder: ...
    def obj_type(self, obj_type: str) -> VersionBuilder: ...
    def parent_type(self, parent_type: str) -> VersionBuilder: ...
    def build(self) -> Version: ...
