from lark_oapi.core.construct import init as init

class AppCommonCategory:
    i18n_key: str | None
    category: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppCommonCategoryBuilder: ...

class AppCommonCategoryBuilder:
    def __init__(self) -> None: ...
    def i18n_key(self, i18n_key: str) -> AppCommonCategoryBuilder: ...
    def category(self, category: str) -> AppCommonCategoryBuilder: ...
    def build(self) -> AppCommonCategory: ...
