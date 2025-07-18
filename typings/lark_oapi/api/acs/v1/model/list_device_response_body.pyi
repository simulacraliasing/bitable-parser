from .device import Device as Device
from lark_oapi.core.construct import init as init

class ListDeviceResponseBody:
    items: list[Device] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListDeviceResponseBodyBuilder: ...

class ListDeviceResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[Device]) -> ListDeviceResponseBodyBuilder: ...
    def build(self) -> ListDeviceResponseBody: ...
