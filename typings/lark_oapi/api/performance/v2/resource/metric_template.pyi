from ..model.query_metric_template_request import QueryMetricTemplateRequest as QueryMetricTemplateRequest
from ..model.query_metric_template_response import QueryMetricTemplateResponse as QueryMetricTemplateResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class MetricTemplate:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def query(self, request: QueryMetricTemplateRequest, option: RequestOption | None = None) -> QueryMetricTemplateResponse: ...
    async def aquery(self, request: QueryMetricTemplateRequest, option: RequestOption | None = None) -> QueryMetricTemplateResponse: ...
