from .post_statistics import PostStatistics as PostStatistics
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2MomentsPostStatisticsUpdatedV1Data:
    post_id: str | None
    statistics_type: int | None
    statistics: PostStatistics | None
    def __init__(self, d=None) -> None: ...

class P2MomentsPostStatisticsUpdatedV1(EventContext):
    event: P2MomentsPostStatisticsUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
