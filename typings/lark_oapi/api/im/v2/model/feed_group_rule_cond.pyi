from .feed_group_rule_cond_item import FeedGroupRuleCondItem as FeedGroupRuleCondItem
from lark_oapi.core.construct import init as init

class FeedGroupRuleCond:
    match_type: str | None
    condition_items: list[FeedGroupRuleCondItem] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FeedGroupRuleCondBuilder: ...

class FeedGroupRuleCondBuilder:
    def __init__(self) -> None: ...
    def match_type(self, match_type: str) -> FeedGroupRuleCondBuilder: ...
    def condition_items(self, condition_items: list[FeedGroupRuleCondItem]) -> FeedGroupRuleCondBuilder: ...
    def build(self) -> FeedGroupRuleCond: ...
