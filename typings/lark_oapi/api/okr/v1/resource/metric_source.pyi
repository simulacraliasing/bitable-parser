from ..model.list_metric_source_request import ListMetricSourceRequest as ListMetricSourceRequest
from ..model.list_metric_source_response import ListMetricSourceResponse as ListMetricSourceResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify

class MetricSource:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListMetricSourceRequest, option: RequestOption | None = None) -> ListMetricSourceResponse: ...
