from .metric_detail import MetricDetail as MetricDetail
from .reviewee_stage_status import RevieweeStageStatus as RevieweeStageStatus
from .user import User as User
from lark_oapi.core.construct import init as init

class RevieweeMetric:
    reviewee_user_id: User | None
    metric_template_id: int | None
    metric_details: MetricDetail | None
    reviewee_stage_statuses: list[RevieweeStageStatus] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RevieweeMetricBuilder: ...

class RevieweeMetricBuilder:
    def __init__(self) -> None: ...
    def reviewee_user_id(self, reviewee_user_id: User) -> RevieweeMetricBuilder: ...
    def metric_template_id(self, metric_template_id: int) -> RevieweeMetricBuilder: ...
    def metric_details(self, metric_details: MetricDetail) -> RevieweeMetricBuilder: ...
    def reviewee_stage_statuses(self, reviewee_stage_statuses: list[RevieweeStageStatus]) -> RevieweeMetricBuilder: ...
    def build(self) -> RevieweeMetric: ...
