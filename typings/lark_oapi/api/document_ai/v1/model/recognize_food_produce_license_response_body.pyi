from .food_produce_license import FoodProduceLicense as FoodProduceLicense
from lark_oapi.core.construct import init as init

class RecognizeFoodProduceLicenseResponseBody:
    food_produce_license: FoodProduceLicense | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RecognizeFoodProduceLicenseResponseBodyBuilder: ...

class RecognizeFoodProduceLicenseResponseBodyBuilder:
    def __init__(self) -> None: ...
    def food_produce_license(self, food_produce_license: FoodProduceLicense) -> RecognizeFoodProduceLicenseResponseBodyBuilder: ...
    def build(self) -> RecognizeFoodProduceLicenseResponseBody: ...
