from ..model.batch_update_metric_source_table_item_request import BatchUpdateMetricSourceTableItemRequest as BatchUpdateMetricSourceTableItemRequest
from ..model.batch_update_metric_source_table_item_response import BatchUpdateMetricSourceTableItemResponse as BatchUpdateMetricSourceTableItemResponse
from ..model.get_metric_source_table_item_request import GetMetricSourceTableItemRequest as GetMetricSourceTableItemRequest
from ..model.get_metric_source_table_item_response import GetMetricSourceTableItemResponse as GetMetricSourceTableItemResponse
from ..model.list_metric_source_table_item_request import ListMetricSourceTableItemRequest as ListMetricSourceTableItemRequest
from ..model.list_metric_source_table_item_response import ListMetricSourceTableItemResponse as ListMetricSourceTableItemResponse
from ..model.patch_metric_source_table_item_request import PatchMetricSourceTableItemRequest as PatchMetricSourceTableItemRequest
from ..model.patch_metric_source_table_item_response import PatchMetricSourceTableItemResponse as PatchMetricSourceTableItemResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify

class MetricSourceTableItem:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_update(self, request: BatchUpdateMetricSourceTableItemRequest, option: RequestOption | None = None) -> BatchUpdateMetricSourceTableItemResponse: ...
    def get(self, request: GetMetricSourceTableItemRequest, option: RequestOption | None = None) -> GetMetricSourceTableItemResponse: ...
    def list(self, request: ListMetricSourceTableItemRequest, option: RequestOption | None = None) -> ListMetricSourceTableItemResponse: ...
    def patch(self, request: PatchMetricSourceTableItemRequest, option: RequestOption | None = None) -> PatchMetricSourceTableItemResponse: ...
