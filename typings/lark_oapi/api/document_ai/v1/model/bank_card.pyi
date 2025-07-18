from .bank_card_entity import BankCardEntity as BankCardEntity
from lark_oapi.core.construct import init as init

class BankCard:
    entities: list[BankCardEntity] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BankCardBuilder: ...

class BankCardBuilder:
    def __init__(self) -> None: ...
    def entities(self, entities: list[BankCardEntity]) -> BankCardBuilder: ...
    def build(self) -> BankCard: ...
