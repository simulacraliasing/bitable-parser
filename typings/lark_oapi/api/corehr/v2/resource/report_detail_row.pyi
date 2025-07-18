from ..model.batch_delete_report_detail_row_request import BatchDeleteReportDetailRowRequest as BatchDeleteReportDetailRowRequest
from ..model.batch_delete_report_detail_row_response import BatchDeleteReportDetailRowResponse as BatchDeleteReportDetailRowResponse
from ..model.batch_save_report_detail_row_request import BatchSaveReportDetailRowRequest as BatchSaveReportDetailRowRequest
from ..model.batch_save_report_detail_row_response import BatchSaveReportDetailRowResponse as BatchSaveReportDetailRowResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ReportDetailRow:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_delete(self, request: BatchDeleteReportDetailRowRequest, option: RequestOption | None = None) -> BatchDeleteReportDetailRowResponse: ...
    async def abatch_delete(self, request: BatchDeleteReportDetailRowRequest, option: RequestOption | None = None) -> BatchDeleteReportDetailRowResponse: ...
    def batch_save(self, request: BatchSaveReportDetailRowRequest, option: RequestOption | None = None) -> BatchSaveReportDetailRowResponse: ...
    async def abatch_save(self, request: BatchSaveReportDetailRowRequest, option: RequestOption | None = None) -> BatchSaveReportDetailRowResponse: ...
