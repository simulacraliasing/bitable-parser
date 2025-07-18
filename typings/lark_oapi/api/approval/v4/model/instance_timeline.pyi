from .file import File as File
from .instance_cc_user import InstanceCcUser as InstanceCcUser
from lark_oapi.core.construct import init as init

class InstanceTimeline:
    type: str | None
    create_time: int | None
    user_id: str | None
    open_id: str | None
    user_id_list: list[str] | None
    open_id_list: list[str] | None
    task_id: str | None
    comment: str | None
    cc_user_list: list[InstanceCcUser] | None
    ext: str | None
    node_key: str | None
    files: list[File] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> InstanceTimelineBuilder: ...

class InstanceTimelineBuilder:
    def __init__(self) -> None: ...
    def type(self, type: str) -> InstanceTimelineBuilder: ...
    def create_time(self, create_time: int) -> InstanceTimelineBuilder: ...
    def user_id(self, user_id: str) -> InstanceTimelineBuilder: ...
    def open_id(self, open_id: str) -> InstanceTimelineBuilder: ...
    def user_id_list(self, user_id_list: list[str]) -> InstanceTimelineBuilder: ...
    def open_id_list(self, open_id_list: list[str]) -> InstanceTimelineBuilder: ...
    def task_id(self, task_id: str) -> InstanceTimelineBuilder: ...
    def comment(self, comment: str) -> InstanceTimelineBuilder: ...
    def cc_user_list(self, cc_user_list: list[InstanceCcUser]) -> InstanceTimelineBuilder: ...
    def ext(self, ext: str) -> InstanceTimelineBuilder: ...
    def node_key(self, node_key: str) -> InstanceTimelineBuilder: ...
    def files(self, files: list[File]) -> InstanceTimelineBuilder: ...
    def build(self) -> InstanceTimeline: ...
