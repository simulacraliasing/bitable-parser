from lark_oapi.core.construct import init as init

class AppCustomCategory:
    i18n_key: str | None
    description: str | None
    app_ids: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppCustomCategoryBuilder: ...

class AppCustomCategoryBuilder:
    def __init__(self) -> None: ...
    def i18n_key(self, i18n_key: str) -> AppCustomCategoryBuilder: ...
    def description(self, description: str) -> AppCustomCategoryBuilder: ...
    def app_ids(self, app_ids: list[str]) -> AppCustomCategoryBuilder: ...
    def build(self) -> AppCustomCategory: ...
