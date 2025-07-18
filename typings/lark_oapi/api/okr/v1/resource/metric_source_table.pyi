from ..model.list_metric_source_table_request import ListMetricSourceTableRequest as ListMetricSourceTableRequest
from ..model.list_metric_source_table_response import ListMetricSourceTableResponse as ListMetricSourceTableResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify

class MetricSourceTable:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListMetricSourceTableRequest, option: RequestOption | None = None) -> ListMetricSourceTableResponse: ...
