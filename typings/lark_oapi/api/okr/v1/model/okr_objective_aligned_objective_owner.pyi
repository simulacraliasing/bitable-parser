from lark_oapi.core.construct import init as init

class OkrObjectiveAlignedObjectiveOwner:
    open_id: str | None
    user_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OkrObjectiveAlignedObjectiveOwnerBuilder: ...

class OkrObjectiveAlignedObjectiveOwnerBuilder:
    def __init__(self) -> None: ...
    def open_id(self, open_id: str) -> OkrObjectiveAlignedObjectiveOwnerBuilder: ...
    def user_id(self, user_id: str) -> OkrObjectiveAlignedObjectiveOwnerBuilder: ...
    def build(self) -> OkrObjectiveAlignedObjectiveOwner: ...
