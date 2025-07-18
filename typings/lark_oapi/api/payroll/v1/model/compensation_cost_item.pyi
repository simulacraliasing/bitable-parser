from .compensation_cost import CompensationCost as CompensationCost
from lark_oapi.core.construct import init as init

class CompensationCostItem:
    number_of_individuals_for_payment: int | None
    compensation_costs: list[CompensationCost] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CompensationCostItemBuilder: ...

class CompensationCostItemBuilder:
    def __init__(self) -> None: ...
    def number_of_individuals_for_payment(self, number_of_individuals_for_payment: int) -> CompensationCostItemBuilder: ...
    def compensation_costs(self, compensation_costs: list[CompensationCost]) -> CompensationCostItemBuilder: ...
    def build(self) -> CompensationCostItem: ...
