from ..model.add_role_assign_authorization_request import AddRoleAssignAuthorizationRequest as AddRoleAssignAuthorizationRequest
from ..model.add_role_assign_authorization_response import AddRoleAssignAuthorizationResponse as AddRoleAssignAuthorizationResponse
from ..model.get_by_param_authorization_request import GetByParamAuthorizationRequest as GetByParamAuthorizationRequest
from ..model.get_by_param_authorization_response import GetByParamAuthorizationResponse as GetByParamAuthorizationResponse
from ..model.query_authorization_request import QueryAuthorizationRequest as QueryAuthorizationRequest
from ..model.query_authorization_response import QueryAuthorizationResponse as QueryAuthorizationResponse
from ..model.remove_role_assign_authorization_request import RemoveRoleAssignAuthorizationRequest as RemoveRoleAssignAuthorizationRequest
from ..model.remove_role_assign_authorization_response import RemoveRoleAssignAuthorizationResponse as RemoveRoleAssignAuthorizationResponse
from ..model.update_role_assign_authorization_request import UpdateRoleAssignAuthorizationRequest as UpdateRoleAssignAuthorizationRequest
from ..model.update_role_assign_authorization_response import UpdateRoleAssignAuthorizationResponse as UpdateRoleAssignAuthorizationResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Authorization:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def add_role_assign(self, request: AddRoleAssignAuthorizationRequest, option: RequestOption | None = None) -> AddRoleAssignAuthorizationResponse: ...
    async def aadd_role_assign(self, request: AddRoleAssignAuthorizationRequest, option: RequestOption | None = None) -> AddRoleAssignAuthorizationResponse: ...
    def get_by_param(self, request: GetByParamAuthorizationRequest, option: RequestOption | None = None) -> GetByParamAuthorizationResponse: ...
    async def aget_by_param(self, request: GetByParamAuthorizationRequest, option: RequestOption | None = None) -> GetByParamAuthorizationResponse: ...
    def query(self, request: QueryAuthorizationRequest, option: RequestOption | None = None) -> QueryAuthorizationResponse: ...
    async def aquery(self, request: QueryAuthorizationRequest, option: RequestOption | None = None) -> QueryAuthorizationResponse: ...
    def remove_role_assign(self, request: RemoveRoleAssignAuthorizationRequest, option: RequestOption | None = None) -> RemoveRoleAssignAuthorizationResponse: ...
    async def aremove_role_assign(self, request: RemoveRoleAssignAuthorizationRequest, option: RequestOption | None = None) -> RemoveRoleAssignAuthorizationResponse: ...
    def update_role_assign(self, request: UpdateRoleAssignAuthorizationRequest, option: RequestOption | None = None) -> UpdateRoleAssignAuthorizationResponse: ...
    async def aupdate_role_assign(self, request: UpdateRoleAssignAuthorizationRequest, option: RequestOption | None = None) -> UpdateRoleAssignAuthorizationResponse: ...
