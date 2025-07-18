from ..model.list_app_workflow_request import ListAppWorkflowRequest as ListAppWorkflowRequest
from ..model.list_app_workflow_response import ListAppWorkflowResponse as ListAppWorkflowResponse
from ..model.update_app_workflow_request import UpdateAppWorkflowRequest as UpdateAppWorkflowRequest
from ..model.update_app_workflow_response import UpdateAppWorkflowResponse as UpdateAppWorkflowResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class AppWorkflow:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListAppWorkflowRequest, option: RequestOption | None = None) -> ListAppWorkflowResponse: ...
    async def alist(self, request: ListAppWorkflowRequest, option: RequestOption | None = None) -> ListAppWorkflowResponse: ...
    def update(self, request: UpdateAppWorkflowRequest, option: RequestOption | None = None) -> UpdateAppWorkflowResponse: ...
    async def aupdate(self, request: UpdateAppWorkflowRequest, option: RequestOption | None = None) -> UpdateAppWorkflowResponse: ...
