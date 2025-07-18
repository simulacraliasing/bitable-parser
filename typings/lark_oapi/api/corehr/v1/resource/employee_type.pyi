from ..model.create_employee_type_request import CreateEmployeeTypeRequest as CreateEmployeeTypeRequest
from ..model.create_employee_type_response import CreateEmployeeTypeResponse as CreateEmployeeTypeResponse
from ..model.delete_employee_type_request import DeleteEmployeeTypeRequest as DeleteEmployeeTypeRequest
from ..model.delete_employee_type_response import DeleteEmployeeTypeResponse as DeleteEmployeeTypeResponse
from ..model.get_employee_type_request import GetEmployeeTypeRequest as GetEmployeeTypeRequest
from ..model.get_employee_type_response import GetEmployeeTypeResponse as GetEmployeeTypeResponse
from ..model.list_employee_type_request import ListEmployeeTypeRequest as ListEmployeeTypeRequest
from ..model.list_employee_type_response import ListEmployeeTypeResponse as ListEmployeeTypeResponse
from ..model.patch_employee_type_request import PatchEmployeeTypeRequest as PatchEmployeeTypeRequest
from ..model.patch_employee_type_response import PatchEmployeeTypeResponse as PatchEmployeeTypeResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class EmployeeType:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateEmployeeTypeRequest, option: RequestOption | None = None) -> CreateEmployeeTypeResponse: ...
    async def acreate(self, request: CreateEmployeeTypeRequest, option: RequestOption | None = None) -> CreateEmployeeTypeResponse: ...
    def delete(self, request: DeleteEmployeeTypeRequest, option: RequestOption | None = None) -> DeleteEmployeeTypeResponse: ...
    async def adelete(self, request: DeleteEmployeeTypeRequest, option: RequestOption | None = None) -> DeleteEmployeeTypeResponse: ...
    def get(self, request: GetEmployeeTypeRequest, option: RequestOption | None = None) -> GetEmployeeTypeResponse: ...
    async def aget(self, request: GetEmployeeTypeRequest, option: RequestOption | None = None) -> GetEmployeeTypeResponse: ...
    def list(self, request: ListEmployeeTypeRequest, option: RequestOption | None = None) -> ListEmployeeTypeResponse: ...
    async def alist(self, request: ListEmployeeTypeRequest, option: RequestOption | None = None) -> ListEmployeeTypeResponse: ...
    def patch(self, request: PatchEmployeeTypeRequest, option: RequestOption | None = None) -> PatchEmployeeTypeResponse: ...
    async def apatch(self, request: PatchEmployeeTypeRequest, option: RequestOption | None = None) -> PatchEmployeeTypeResponse: ...
