from .drving_license import DrvingLicense as DrvingLicense
from lark_oapi.core.construct import init as init

class RecognizeDrivingLicenseResponseBody:
    driving_license: DrvingLicense | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RecognizeDrivingLicenseResponseBodyBuilder: ...

class RecognizeDrivingLicenseResponseBodyBuilder:
    def __init__(self) -> None: ...
    def driving_license(self, driving_license: DrvingLicense) -> RecognizeDrivingLicenseResponseBodyBuilder: ...
    def build(self) -> RecognizeDrivingLicenseResponseBody: ...
