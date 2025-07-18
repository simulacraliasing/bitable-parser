from ..model.list_app_table_form_field_request import ListAppTableFormFieldRequest as ListAppTableFormFieldRequest
from ..model.list_app_table_form_field_response import ListAppTableFormFieldResponse as ListAppTableFormFieldResponse
from ..model.patch_app_table_form_field_request import PatchAppTableFormFieldRequest as PatchAppTableFormFieldRequest
from ..model.patch_app_table_form_field_response import PatchAppTableFormFieldResponse as PatchAppTableFormFieldResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class AppTableFormField:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListAppTableFormFieldRequest, option: RequestOption | None = None) -> ListAppTableFormFieldResponse: ...
    async def alist(self, request: ListAppTableFormFieldRequest, option: RequestOption | None = None) -> ListAppTableFormFieldResponse: ...
    def patch(self, request: PatchAppTableFormFieldRequest, option: RequestOption | None = None) -> PatchAppTableFormFieldResponse: ...
    async def apatch(self, request: PatchAppTableFormFieldRequest, option: RequestOption | None = None) -> PatchAppTableFormFieldResponse: ...
