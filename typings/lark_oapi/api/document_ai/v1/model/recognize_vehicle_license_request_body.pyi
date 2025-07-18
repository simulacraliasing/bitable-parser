from lark_oapi.core.construct import init as init
from typing import Any, IO

class RecognizeVehicleLicenseRequestBody:
    file: IO[Any] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RecognizeVehicleLicenseRequestBodyBuilder: ...

class RecognizeVehicleLicenseRequestBodyBuilder:
    def __init__(self) -> None: ...
    def file(self, file: IO[Any]) -> RecognizeVehicleLicenseRequestBodyBuilder: ...
    def build(self) -> RecognizeVehicleLicenseRequestBody: ...
