from lark_oapi.core.construct import init as init

class BackgroundCheckProcessInfo:
    process: str | None
    update_time: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BackgroundCheckProcessInfoBuilder: ...

class BackgroundCheckProcessInfoBuilder:
    def __init__(self) -> None: ...
    def process(self, process: str) -> BackgroundCheckProcessInfoBuilder: ...
    def update_time(self, update_time: str) -> BackgroundCheckProcessInfoBuilder: ...
    def build(self) -> BackgroundCheckProcessInfo: ...
