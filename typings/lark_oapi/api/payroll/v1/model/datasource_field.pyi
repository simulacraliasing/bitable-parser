from .i18n_content import I18nContent as I18nContent
from lark_oapi.core.construct import init as init

class DatasourceField:
    code: str | None
    i18n_names: list[I18nContent] | None
    field_type: int | None
    active_status: int | None
    i18n_description: list[I18nContent] | None
    decimal_places: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DatasourceFieldBuilder: ...

class DatasourceFieldBuilder:
    def __init__(self) -> None: ...
    def code(self, code: str) -> DatasourceFieldBuilder: ...
    def i18n_names(self, i18n_names: list[I18nContent]) -> DatasourceFieldBuilder: ...
    def field_type(self, field_type: int) -> DatasourceFieldBuilder: ...
    def active_status(self, active_status: int) -> DatasourceFieldBuilder: ...
    def i18n_description(self, i18n_description: list[I18nContent]) -> DatasourceFieldBuilder: ...
    def decimal_places(self, decimal_places: int) -> DatasourceFieldBuilder: ...
    def build(self) -> DatasourceField: ...
