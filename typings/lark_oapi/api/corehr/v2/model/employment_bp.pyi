from lark_oapi.core.construct import init as init

class EmploymentBp:
    employment_id: str | None
    hrbp_ids: list[str] | None
    location_bp_ids: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EmploymentBpBuilder: ...

class EmploymentBpBuilder:
    def __init__(self) -> None: ...
    def employment_id(self, employment_id: str) -> EmploymentBpBuilder: ...
    def hrbp_ids(self, hrbp_ids: list[str]) -> EmploymentBpBuilder: ...
    def location_bp_ids(self, location_bp_ids: list[str]) -> EmploymentBpBuilder: ...
    def build(self) -> EmploymentBp: ...
