from lark_oapi.core.construct import init as init

class AppVisibleList:
    open_ids: list[int] | None
    department_ids: list[int] | None
    group_ids: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppVisibleListBuilder: ...

class AppVisibleListBuilder:
    def __init__(self) -> None: ...
    def open_ids(self, open_ids: list[int]) -> AppVisibleListBuilder: ...
    def department_ids(self, department_ids: list[int]) -> AppVisibleListBuilder: ...
    def group_ids(self, group_ids: list[str]) -> AppVisibleListBuilder: ...
    def build(self) -> AppVisibleList: ...
