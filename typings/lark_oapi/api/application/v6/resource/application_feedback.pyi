from ..model.list_application_feedback_request import ListApplicationFeedbackRequest as ListApplicationFeedbackRequest
from ..model.list_application_feedback_response import ListApplicationFeedbackResponse as ListApplicationFeedbackResponse
from ..model.patch_application_feedback_request import PatchApplicationFeedbackRequest as PatchApplicationFeedbackRequest
from ..model.patch_application_feedback_response import PatchApplicationFeedbackResponse as PatchApplicationFeedbackResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ApplicationFeedback:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListApplicationFeedbackRequest, option: RequestOption | None = None) -> ListApplicationFeedbackResponse: ...
    async def alist(self, request: ListApplicationFeedbackRequest, option: RequestOption | None = None) -> ListApplicationFeedbackResponse: ...
    def patch(self, request: PatchApplicationFeedbackRequest, option: RequestOption | None = None) -> PatchApplicationFeedbackResponse: ...
    async def apatch(self, request: PatchApplicationFeedbackRequest, option: RequestOption | None = None) -> PatchApplicationFeedbackResponse: ...
