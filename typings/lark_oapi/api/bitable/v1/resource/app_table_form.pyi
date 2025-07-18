from ..model.get_app_table_form_request import GetAppTableFormRequest as GetAppTableFormRequest
from ..model.get_app_table_form_response import GetAppTableFormResponse as GetAppTableFormResponse
from ..model.patch_app_table_form_request import PatchAppTableFormRequest as PatchAppTableFormRequest
from ..model.patch_app_table_form_response import PatchAppTableFormResponse as PatchAppTableFormResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class AppTableForm:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetAppTableFormRequest, option: RequestOption | None = None) -> GetAppTableFormResponse: ...
    async def aget(self, request: GetAppTableFormRequest, option: RequestOption | None = None) -> GetAppTableFormResponse: ...
    def patch(self, request: PatchAppTableFormRequest, option: RequestOption | None = None) -> PatchAppTableFormResponse: ...
    async def apatch(self, request: PatchAppTableFormRequest, option: RequestOption | None = None) -> PatchAppTableFormResponse: ...
