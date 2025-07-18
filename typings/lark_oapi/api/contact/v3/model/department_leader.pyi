from lark_oapi.core.construct import init as init

class DepartmentLeader:
    leader_type: int | None
    leader_i_d: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DepartmentLeaderBuilder: ...

class DepartmentLeaderBuilder:
    def __init__(self) -> None: ...
    def leader_type(self, leader_type: int) -> DepartmentLeaderBuilder: ...
    def leader_i_d(self, leader_i_d: str) -> DepartmentLeaderBuilder: ...
    def build(self) -> DepartmentLeader: ...
