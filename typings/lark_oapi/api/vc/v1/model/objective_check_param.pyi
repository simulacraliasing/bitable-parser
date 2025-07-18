from lark_oapi.core.construct import init as init

class ObjectiveCheckParam:
    params: list[int] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ObjectiveCheckParamBuilder: ...

class ObjectiveCheckParamBuilder:
    def __init__(self) -> None: ...
    def params(self, params: list[int]) -> ObjectiveCheckParamBuilder: ...
    def build(self) -> ObjectiveCheckParam: ...
