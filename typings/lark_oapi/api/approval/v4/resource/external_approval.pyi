from ..model.create_external_approval_request import CreateExternalApprovalRequest as CreateExternalApprovalRequest
from ..model.create_external_approval_response import CreateExternalApprovalResponse as CreateExternalApprovalResponse
from ..model.get_external_approval_request import GetExternalApprovalRequest as GetExternalApprovalRequest
from ..model.get_external_approval_response import GetExternalApprovalResponse as GetExternalApprovalResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ExternalApproval:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateExternalApprovalRequest, option: RequestOption | None = None) -> CreateExternalApprovalResponse: ...
    async def acreate(self, request: CreateExternalApprovalRequest, option: RequestOption | None = None) -> CreateExternalApprovalResponse: ...
    def get(self, request: GetExternalApprovalRequest, option: RequestOption | None = None) -> GetExternalApprovalResponse: ...
    async def aget(self, request: GetExternalApprovalRequest, option: RequestOption | None = None) -> GetExternalApprovalResponse: ...
