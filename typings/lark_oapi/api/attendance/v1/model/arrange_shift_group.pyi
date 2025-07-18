from lark_oapi.core.construct import init as init

class ArrangeShiftGroup:
    shift_group_id: int | None
    group_id: int | None
    shift_group_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ArrangeShiftGroupBuilder: ...

class ArrangeShiftGroupBuilder:
    def __init__(self) -> None: ...
    def shift_group_id(self, shift_group_id: int) -> ArrangeShiftGroupBuilder: ...
    def group_id(self, group_id: int) -> ArrangeShiftGroupBuilder: ...
    def shift_group_name(self, shift_group_name: str) -> ArrangeShiftGroupBuilder: ...
    def build(self) -> ArrangeShiftGroup: ...
