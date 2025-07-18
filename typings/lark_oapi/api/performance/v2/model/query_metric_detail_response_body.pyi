from .reviewee_metric import RevieweeMetric as RevieweeMetric
from lark_oapi.core.construct import init as init

class QueryMetricDetailResponseBody:
    semester_id: str | None
    reviewee_metrics: list[RevieweeMetric] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryMetricDetailResponseBodyBuilder: ...

class QueryMetricDetailResponseBodyBuilder:
    def __init__(self) -> None: ...
    def semester_id(self, semester_id: str) -> QueryMetricDetailResponseBodyBuilder: ...
    def reviewee_metrics(self, reviewee_metrics: list[RevieweeMetric]) -> QueryMetricDetailResponseBodyBuilder: ...
    def build(self) -> QueryMetricDetailResponseBody: ...
