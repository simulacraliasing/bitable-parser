from ..model.create_custom_field_option_request import CreateCustomFieldOptionRequest as CreateCustomFieldOptionRequest
from ..model.create_custom_field_option_response import CreateCustomFieldOptionResponse as CreateCustomFieldOptionResponse
from ..model.patch_custom_field_option_request import PatchCustomFieldOptionRequest as PatchCustomFieldOptionRequest
from ..model.patch_custom_field_option_response import PatchCustomFieldOptionResponse as PatchCustomFieldOptionResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class CustomFieldOption:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateCustomFieldOptionRequest, option: RequestOption | None = None) -> CreateCustomFieldOptionResponse: ...
    async def acreate(self, request: CreateCustomFieldOptionRequest, option: RequestOption | None = None) -> CreateCustomFieldOptionResponse: ...
    def patch(self, request: PatchCustomFieldOptionRequest, option: RequestOption | None = None) -> PatchCustomFieldOptionResponse: ...
    async def apatch(self, request: PatchCustomFieldOptionRequest, option: RequestOption | None = None) -> PatchCustomFieldOptionResponse: ...
