from .app_table_view_property_filter_info import AppTableViewPropertyFilterInfo as AppTableViewPropertyFilterInfo
from .app_table_view_property_hierarchy_config import AppTableViewPropertyHierarchyConfig as AppTableViewPropertyHierarchyConfig
from lark_oapi.core.construct import init as init

class AppTableViewProperty:
    filter_info: AppTableViewPropertyFilterInfo | None
    hidden_fields: list[str] | None
    hierarchy_config: AppTableViewPropertyHierarchyConfig | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppTableViewPropertyBuilder: ...

class AppTableViewPropertyBuilder:
    def __init__(self) -> None: ...
    def filter_info(self, filter_info: AppTableViewPropertyFilterInfo) -> AppTableViewPropertyBuilder: ...
    def hidden_fields(self, hidden_fields: list[str]) -> AppTableViewPropertyBuilder: ...
    def hierarchy_config(self, hierarchy_config: AppTableViewPropertyHierarchyConfig) -> AppTableViewPropertyBuilder: ...
    def build(self) -> AppTableViewProperty: ...
