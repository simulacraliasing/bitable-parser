from lark_oapi.core.construct import init as init

class WebPassageParam:
    searchable: bool | None
    domains: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> WebPassageParamBuilder: ...

class WebPassageParamBuilder:
    def __init__(self) -> None: ...
    def searchable(self, searchable: bool) -> WebPassageParamBuilder: ...
    def domains(self, domains: list[str]) -> WebPassageParamBuilder: ...
    def build(self) -> WebPassageParam: ...
