from .external_instance_link import ExternalInstanceLink as ExternalInstanceLink
from lark_oapi.core.construct import init as init

class CcNode:
    cc_id: str | None
    user_id: str | None
    open_id: str | None
    links: ExternalInstanceLink | None
    read_status: str | None
    extra: str | None
    title: str | None
    create_time: int | None
    update_time: int | None
    display_method: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CcNodeBuilder: ...

class CcNodeBuilder:
    def __init__(self) -> None: ...
    def cc_id(self, cc_id: str) -> CcNodeBuilder: ...
    def user_id(self, user_id: str) -> CcNodeBuilder: ...
    def open_id(self, open_id: str) -> CcNodeBuilder: ...
    def links(self, links: ExternalInstanceLink) -> CcNodeBuilder: ...
    def read_status(self, read_status: str) -> CcNodeBuilder: ...
    def extra(self, extra: str) -> CcNodeBuilder: ...
    def title(self, title: str) -> CcNodeBuilder: ...
    def create_time(self, create_time: int) -> CcNodeBuilder: ...
    def update_time(self, update_time: int) -> CcNodeBuilder: ...
    def display_method(self, display_method: str) -> CcNodeBuilder: ...
    def build(self) -> CcNode: ...
