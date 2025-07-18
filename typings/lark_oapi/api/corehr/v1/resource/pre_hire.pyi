from ..model.delete_pre_hire_request import DeletePreHireRequest as DeletePreHireRequest
from ..model.delete_pre_hire_response import DeletePreHireResponse as DeletePreHireResponse
from ..model.get_pre_hire_request import GetPreHireRequest as GetPreHireRequest
from ..model.get_pre_hire_response import GetPreHireResponse as GetPreHireResponse
from ..model.list_pre_hire_request import ListPreHireRequest as ListPreHireRequest
from ..model.list_pre_hire_response import ListPreHireResponse as ListPreHireResponse
from ..model.patch_pre_hire_request import PatchPreHireRequest as PatchPreHireRequest
from ..model.patch_pre_hire_response import PatchPreHireResponse as PatchPreHireResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class PreHire:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def delete(self, request: DeletePreHireRequest, option: RequestOption | None = None) -> DeletePreHireResponse: ...
    async def adelete(self, request: DeletePreHireRequest, option: RequestOption | None = None) -> DeletePreHireResponse: ...
    def get(self, request: GetPreHireRequest, option: RequestOption | None = None) -> GetPreHireResponse: ...
    async def aget(self, request: GetPreHireRequest, option: RequestOption | None = None) -> GetPreHireResponse: ...
    def list(self, request: ListPreHireRequest, option: RequestOption | None = None) -> ListPreHireResponse: ...
    async def alist(self, request: ListPreHireRequest, option: RequestOption | None = None) -> ListPreHireResponse: ...
    def patch(self, request: PatchPreHireRequest, option: RequestOption | None = None) -> PatchPreHireResponse: ...
    async def apatch(self, request: PatchPreHireRequest, option: RequestOption | None = None) -> PatchPreHireResponse: ...
