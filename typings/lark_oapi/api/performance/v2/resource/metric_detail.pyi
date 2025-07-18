from ..model.import_metric_detail_request import ImportMetricDetailRequest as ImportMetricDetailRequest
from ..model.import_metric_detail_response import ImportMetricDetailResponse as ImportMetricDetailResponse
from ..model.query_metric_detail_request import QueryMetricDetailRequest as QueryMetricDetailRequest
from ..model.query_metric_detail_response import QueryMetricDetailResponse as QueryMetricDetailResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class MetricDetail:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def import_(self, request: ImportMetricDetailRequest, option: RequestOption | None = None) -> ImportMetricDetailResponse: ...
    async def aimport_(self, request: ImportMetricDetailRequest, option: RequestOption | None = None) -> ImportMetricDetailResponse: ...
    def query(self, request: QueryMetricDetailRequest, option: RequestOption | None = None) -> QueryMetricDetailResponse: ...
    async def aquery(self, request: QueryMetricDetailRequest, option: RequestOption | None = None) -> QueryMetricDetailResponse: ...
