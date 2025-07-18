from ..model.create_draft_request import CreateDraftRequest as CreateDraftRequest
from ..model.create_draft_response import CreateDraftResponse as CreateDraftResponse
from ..model.update_draft_request import UpdateDraftRequest as UpdateDraftRequest
from ..model.update_draft_response import UpdateDraftResponse as UpdateDraftResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Draft:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateDraftRequest, option: RequestOption | None = None) -> CreateDraftResponse: ...
    async def acreate(self, request: CreateDraftRequest, option: RequestOption | None = None) -> CreateDraftResponse: ...
    def update(self, request: UpdateDraftRequest, option: RequestOption | None = None) -> UpdateDraftResponse: ...
    async def aupdate(self, request: UpdateDraftRequest, option: RequestOption | None = None) -> UpdateDraftResponse: ...
