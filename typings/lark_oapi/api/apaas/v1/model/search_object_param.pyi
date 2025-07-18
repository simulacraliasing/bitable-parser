from .criterion import Criterion as Criterion
from .order_condition import OrderCondition as OrderCondition
from lark_oapi.core.construct import init as init

class SearchObjectParam:
    api_name: str | None
    search_fields: list[str] | None
    select: list[str] | None
    filter: Criterion | None
    order_by: OrderCondition | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchObjectParamBuilder: ...

class SearchObjectParamBuilder:
    def __init__(self) -> None: ...
    def api_name(self, api_name: str) -> SearchObjectParamBuilder: ...
    def search_fields(self, search_fields: list[str]) -> SearchObjectParamBuilder: ...
    def select(self, select: list[str]) -> SearchObjectParamBuilder: ...
    def filter(self, filter: Criterion) -> SearchObjectParamBuilder: ...
    def order_by(self, order_by: OrderCondition) -> SearchObjectParamBuilder: ...
    def build(self) -> SearchObjectParam: ...
