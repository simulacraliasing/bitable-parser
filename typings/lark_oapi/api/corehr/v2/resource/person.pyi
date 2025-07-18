from ..model.create_person_request import CreatePersonRequest as CreatePersonRequest
from ..model.create_person_response import CreatePersonResponse as CreatePersonResponse
from ..model.patch_person_request import PatchPersonRequest as PatchPersonRequest
from ..model.patch_person_response import PatchPersonResponse as PatchPersonResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Person:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreatePersonRequest, option: RequestOption | None = None) -> CreatePersonResponse: ...
    async def acreate(self, request: CreatePersonRequest, option: RequestOption | None = None) -> CreatePersonResponse: ...
    def patch(self, request: PatchPersonRequest, option: RequestOption | None = None) -> PatchPersonResponse: ...
    async def apatch(self, request: PatchPersonRequest, option: RequestOption | None = None) -> PatchPersonResponse: ...
