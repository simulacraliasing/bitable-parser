from lark_oapi.core.construct import init as init

class ApplicationPrehireDepartment:
    id: str | None
    name: str | None
    en_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ApplicationPrehireDepartmentBuilder: ...

class ApplicationPrehireDepartmentBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> ApplicationPrehireDepartmentBuilder: ...
    def name(self, name: str) -> ApplicationPrehireDepartmentBuilder: ...
    def en_name(self, en_name: str) -> ApplicationPrehireDepartmentBuilder: ...
    def build(self) -> ApplicationPrehireDepartment: ...
