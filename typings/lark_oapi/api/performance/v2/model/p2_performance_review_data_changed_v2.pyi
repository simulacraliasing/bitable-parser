from .review_data_change import ReviewDataChange as ReviewDataChange
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2PerformanceReviewDataChangedV2Data:
    items: list[ReviewDataChange] | None
    def __init__(self, d=None) -> None: ...

class P2PerformanceReviewDataChangedV2(EventContext):
    event: P2PerformanceReviewDataChangedV2Data | None
    def __init__(self, d=None) -> None: ...
