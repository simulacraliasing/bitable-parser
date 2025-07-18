from .food_manage_entity import FoodManageEntity as FoodManageEntity
from lark_oapi.core.construct import init as init

class FoodManageLicense:
    entities: list[FoodManageEntity] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FoodManageLicenseBuilder: ...

class FoodManageLicenseBuilder:
    def __init__(self) -> None: ...
    def entities(self, entities: list[FoodManageEntity]) -> FoodManageLicenseBuilder: ...
    def build(self) -> FoodManageLicense: ...
