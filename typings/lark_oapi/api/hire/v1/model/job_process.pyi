from lark_oapi.core.construct import init as init

class JobProcess:
    your_property_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> JobProcessBuilder: ...

class JobProcessBuilder:
    def __init__(self) -> None: ...
    def your_property_name(self, your_property_name: str) -> JobProcessBuilder: ...
    def build(self) -> JobProcess: ...
