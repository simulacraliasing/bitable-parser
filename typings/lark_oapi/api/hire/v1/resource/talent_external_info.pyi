from ..model.create_talent_external_info_request import CreateTalentExternalInfoRequest as CreateTalentExternalInfoRequest
from ..model.create_talent_external_info_response import CreateTalentExternalInfoResponse as CreateTalentExternalInfoResponse
from ..model.update_talent_external_info_request import UpdateTalentExternalInfoRequest as UpdateTalentExternalInfoRequest
from ..model.update_talent_external_info_response import UpdateTalentExternalInfoResponse as UpdateTalentExternalInfoResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class TalentExternalInfo:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateTalentExternalInfoRequest, option: RequestOption | None = None) -> CreateTalentExternalInfoResponse: ...
    async def acreate(self, request: CreateTalentExternalInfoRequest, option: RequestOption | None = None) -> CreateTalentExternalInfoResponse: ...
    def update(self, request: UpdateTalentExternalInfoRequest, option: RequestOption | None = None) -> UpdateTalentExternalInfoResponse: ...
    async def aupdate(self, request: UpdateTalentExternalInfoRequest, option: RequestOption | None = None) -> UpdateTalentExternalInfoResponse: ...
