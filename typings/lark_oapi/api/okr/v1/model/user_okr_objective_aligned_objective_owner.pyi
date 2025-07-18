from lark_oapi.core.construct import init as init

class UserOkrObjectiveAlignedObjectiveOwner:
    open_id: str | None
    employee_id: str | None
    employee_no: str | None
    union_id: str | None
    name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UserOkrObjectiveAlignedObjectiveOwnerBuilder: ...

class UserOkrObjectiveAlignedObjectiveOwnerBuilder:
    def __init__(self) -> None: ...
    def open_id(self, open_id: str) -> UserOkrObjectiveAlignedObjectiveOwnerBuilder: ...
    def employee_id(self, employee_id: str) -> UserOkrObjectiveAlignedObjectiveOwnerBuilder: ...
    def employee_no(self, employee_no: str) -> UserOkrObjectiveAlignedObjectiveOwnerBuilder: ...
    def union_id(self, union_id: str) -> UserOkrObjectiveAlignedObjectiveOwnerBuilder: ...
    def name(self, name: str) -> UserOkrObjectiveAlignedObjectiveOwnerBuilder: ...
    def build(self) -> UserOkrObjectiveAlignedObjectiveOwner: ...
