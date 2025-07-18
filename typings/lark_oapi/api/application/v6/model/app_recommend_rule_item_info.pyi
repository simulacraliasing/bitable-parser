from .app_recommend_rule_item_info_i18n_name import AppRecommendRuleItemInfoI18nName as AppRecommendRuleItemInfoI18nName
from lark_oapi.core.construct import init as init

class AppRecommendRuleItemInfo:
    item_id: str | None
    item_type: str | None
    name: str | None
    description: str | None
    link_url: str | None
    client_id: str | None
    icon_url: str | None
    default_locale: str | None
    i18n_name: AppRecommendRuleItemInfoI18nName | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppRecommendRuleItemInfoBuilder: ...

class AppRecommendRuleItemInfoBuilder:
    def __init__(self) -> None: ...
    def item_id(self, item_id: str) -> AppRecommendRuleItemInfoBuilder: ...
    def item_type(self, item_type: str) -> AppRecommendRuleItemInfoBuilder: ...
    def name(self, name: str) -> AppRecommendRuleItemInfoBuilder: ...
    def description(self, description: str) -> AppRecommendRuleItemInfoBuilder: ...
    def link_url(self, link_url: str) -> AppRecommendRuleItemInfoBuilder: ...
    def client_id(self, client_id: str) -> AppRecommendRuleItemInfoBuilder: ...
    def icon_url(self, icon_url: str) -> AppRecommendRuleItemInfoBuilder: ...
    def default_locale(self, default_locale: str) -> AppRecommendRuleItemInfoBuilder: ...
    def i18n_name(self, i18n_name: AppRecommendRuleItemInfoI18nName) -> AppRecommendRuleItemInfoBuilder: ...
    def build(self) -> AppRecommendRuleItemInfo: ...
