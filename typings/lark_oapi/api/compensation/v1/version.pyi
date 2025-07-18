from .resource import *

class V1:
    archive: Archive
    change_reason: ChangeReason
    indicator: Indicator
    item: Item
    item_category: ItemCategory
    plan: Plan
    def __init__(self, config: Config) -> None: ...
