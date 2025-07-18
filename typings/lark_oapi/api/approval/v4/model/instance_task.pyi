from lark_oapi.core.construct import init as init

class InstanceTask:
    id: str | None
    user_id: str | None
    open_id: str | None
    status: str | None
    node_id: str | None
    node_name: str | None
    custom_node_id: str | None
    type: str | None
    start_time: int | None
    end_time: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> InstanceTaskBuilder: ...

class InstanceTaskBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> InstanceTaskBuilder: ...
    def user_id(self, user_id: str) -> InstanceTaskBuilder: ...
    def open_id(self, open_id: str) -> InstanceTaskBuilder: ...
    def status(self, status: str) -> InstanceTaskBuilder: ...
    def node_id(self, node_id: str) -> InstanceTaskBuilder: ...
    def node_name(self, node_name: str) -> InstanceTaskBuilder: ...
    def custom_node_id(self, custom_node_id: str) -> InstanceTaskBuilder: ...
    def type(self, type: str) -> InstanceTaskBuilder: ...
    def start_time(self, start_time: int) -> InstanceTaskBuilder: ...
    def end_time(self, end_time: int) -> InstanceTaskBuilder: ...
    def build(self) -> InstanceTask: ...
