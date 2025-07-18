from lark_oapi.core.construct import init as init

class Process:
    id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ProcessBuilder: ...

class ProcessBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> ProcessBuilder: ...
    def build(self) -> Process: ...
