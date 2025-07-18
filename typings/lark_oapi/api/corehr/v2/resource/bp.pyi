from ..model.get_by_department_bp_request import GetByDepartmentBpRequest as GetByDepartmentBpRequest
from ..model.get_by_department_bp_response import GetByDepartmentBpResponse as GetByDepartmentBpResponse
from ..model.list_bp_request import ListBpRequest as ListBpRequest
from ..model.list_bp_response import ListBpResponse as ListBpResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Bp:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get_by_department(self, request: GetByDepartmentBpRequest, option: RequestOption | None = None) -> GetByDepartmentBpResponse: ...
    async def aget_by_department(self, request: GetByDepartmentBpRequest, option: RequestOption | None = None) -> GetByDepartmentBpResponse: ...
    def list(self, request: ListBpRequest, option: RequestOption | None = None) -> ListBpResponse: ...
    async def alist(self, request: ListBpRequest, option: RequestOption | None = None) -> ListBpResponse: ...
