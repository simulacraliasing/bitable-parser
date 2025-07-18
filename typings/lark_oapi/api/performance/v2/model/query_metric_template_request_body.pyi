from lark_oapi.core.construct import init as init

class QueryMetricTemplateRequestBody:
    metrics_template_ids: list[int] | None
    status: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryMetricTemplateRequestBodyBuilder: ...

class QueryMetricTemplateRequestBodyBuilder:
    def __init__(self) -> None: ...
    def metrics_template_ids(self, metrics_template_ids: list[int]) -> QueryMetricTemplateRequestBodyBuilder: ...
    def status(self, status: str) -> QueryMetricTemplateRequestBodyBuilder: ...
    def build(self) -> QueryMetricTemplateRequestBody: ...
