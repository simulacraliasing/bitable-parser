from lark_oapi.core.construct import init as init

class View:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ViewBuilder: ...

class ViewBuilder:
    def __init__(self) -> None: ...
    def build(self) -> View: ...
