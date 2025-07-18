from ..model.create_tag_request import CreateTagRequest as CreateTagRequest
from ..model.create_tag_response import CreateTagResponse as CreateTagResponse
from ..model.patch_tag_request import PatchTagRequest as PatchTagRequest
from ..model.patch_tag_response import PatchTagResponse as PatchTagResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Tag:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateTagRequest, option: RequestOption | None = None) -> CreateTagResponse: ...
    async def acreate(self, request: CreateTagRequest, option: RequestOption | None = None) -> CreateTagResponse: ...
    def patch(self, request: PatchTagRequest, option: RequestOption | None = None) -> PatchTagResponse: ...
    async def apatch(self, request: PatchTagRequest, option: RequestOption | None = None) -> PatchTagResponse: ...
