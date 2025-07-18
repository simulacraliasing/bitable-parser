from ..model.check_white_black_list_application_visibility_request import CheckWhiteBlackListApplicationVisibilityRequest as CheckWhiteBlackListApplicationVisibilityRequest
from ..model.check_white_black_list_application_visibility_response import CheckWhiteBlackListApplicationVisibilityResponse as CheckWhiteBlackListApplicationVisibilityResponse
from ..model.patch_application_visibility_request import PatchApplicationVisibilityRequest as PatchApplicationVisibilityRequest
from ..model.patch_application_visibility_response import PatchApplicationVisibilityResponse as PatchApplicationVisibilityResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ApplicationVisibility:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def check_white_black_list(self, request: CheckWhiteBlackListApplicationVisibilityRequest, option: RequestOption | None = None) -> CheckWhiteBlackListApplicationVisibilityResponse: ...
    async def acheck_white_black_list(self, request: CheckWhiteBlackListApplicationVisibilityRequest, option: RequestOption | None = None) -> CheckWhiteBlackListApplicationVisibilityResponse: ...
    def patch(self, request: PatchApplicationVisibilityRequest, option: RequestOption | None = None) -> PatchApplicationVisibilityResponse: ...
    async def apatch(self, request: PatchApplicationVisibilityRequest, option: RequestOption | None = None) -> PatchApplicationVisibilityResponse: ...
