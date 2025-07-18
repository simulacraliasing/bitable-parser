from .id_with_name import IdWithName as IdWithName
from .verif_datasource_item import VerifDatasourceItem as VerifDatasourceItem
from lark_oapi.core.construct import init as init

class VerifDataSourceRule:
    api_name: str | None
    datasource_name: IdWithName | None
    object_type: int | None
    datasource_items: list[VerifDatasourceItem] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> VerifDataSourceRuleBuilder: ...

class VerifDataSourceRuleBuilder:
    def __init__(self) -> None: ...
    def api_name(self, api_name: str) -> VerifDataSourceRuleBuilder: ...
    def datasource_name(self, datasource_name: IdWithName) -> VerifDataSourceRuleBuilder: ...
    def object_type(self, object_type: int) -> VerifDataSourceRuleBuilder: ...
    def datasource_items(self, datasource_items: list[VerifDatasourceItem]) -> VerifDataSourceRuleBuilder: ...
    def build(self) -> VerifDataSourceRule: ...
