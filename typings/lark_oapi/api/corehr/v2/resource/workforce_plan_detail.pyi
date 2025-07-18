from ..model.batch_v2_workforce_plan_detail_request import BatchV2WorkforcePlanDetailRequest as BatchV2WorkforcePlanDetailRequest
from ..model.batch_v2_workforce_plan_detail_response import BatchV2WorkforcePlanDetailResponse as BatchV2WorkforcePlanDetailResponse
from ..model.batch_workforce_plan_detail_request import BatchWorkforcePlanDetailRequest as BatchWorkforcePlanDetailRequest
from ..model.batch_workforce_plan_detail_response import BatchWorkforcePlanDetailResponse as BatchWorkforcePlanDetailResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class WorkforcePlanDetail:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch(self, request: BatchWorkforcePlanDetailRequest, option: RequestOption | None = None) -> BatchWorkforcePlanDetailResponse: ...
    async def abatch(self, request: BatchWorkforcePlanDetailRequest, option: RequestOption | None = None) -> BatchWorkforcePlanDetailResponse: ...
    def batch_v2(self, request: BatchV2WorkforcePlanDetailRequest, option: RequestOption | None = None) -> BatchV2WorkforcePlanDetailResponse: ...
    async def abatch_v2(self, request: BatchV2WorkforcePlanDetailRequest, option: RequestOption | None = None) -> BatchV2WorkforcePlanDetailResponse: ...
