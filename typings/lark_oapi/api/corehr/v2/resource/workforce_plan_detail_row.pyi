from ..model.batch_delete_workforce_plan_detail_row_request import BatchDeleteWorkforcePlanDetailRowRequest as BatchDeleteWorkforcePlanDetailRowRequest
from ..model.batch_delete_workforce_plan_detail_row_response import BatchDeleteWorkforcePlanDetailRowResponse as BatchDeleteWorkforcePlanDetailRowResponse
from ..model.batch_save_workforce_plan_detail_row_request import BatchSaveWorkforcePlanDetailRowRequest as BatchSaveWorkforcePlanDetailRowRequest
from ..model.batch_save_workforce_plan_detail_row_response import BatchSaveWorkforcePlanDetailRowResponse as BatchSaveWorkforcePlanDetailRowResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class WorkforcePlanDetailRow:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_delete(self, request: BatchDeleteWorkforcePlanDetailRowRequest, option: RequestOption | None = None) -> BatchDeleteWorkforcePlanDetailRowResponse: ...
    async def abatch_delete(self, request: BatchDeleteWorkforcePlanDetailRowRequest, option: RequestOption | None = None) -> BatchDeleteWorkforcePlanDetailRowResponse: ...
    def batch_save(self, request: BatchSaveWorkforcePlanDetailRowRequest, option: RequestOption | None = None) -> BatchSaveWorkforcePlanDetailRowResponse: ...
    async def abatch_save(self, request: BatchSaveWorkforcePlanDetailRowRequest, option: RequestOption | None = None) -> BatchSaveWorkforcePlanDetailRowResponse: ...
