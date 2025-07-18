from .i18n_content import I18nContent as I18nContent
from lark_oapi.core.construct import init as init

class AcctItem:
    id: str | None
    i18n_names: list[I18nContent] | None
    category_id: str | None
    data_type: int | None
    decimal_places: int | None
    active_status: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AcctItemBuilder: ...

class AcctItemBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> AcctItemBuilder: ...
    def i18n_names(self, i18n_names: list[I18nContent]) -> AcctItemBuilder: ...
    def category_id(self, category_id: str) -> AcctItemBuilder: ...
    def data_type(self, data_type: int) -> AcctItemBuilder: ...
    def decimal_places(self, decimal_places: int) -> AcctItemBuilder: ...
    def active_status(self, active_status: int) -> AcctItemBuilder: ...
    def build(self) -> AcctItem: ...
