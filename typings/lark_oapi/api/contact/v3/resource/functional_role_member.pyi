from ..model.batch_create_functional_role_member_request import BatchCreateFunctionalRoleMemberRequest as BatchCreateFunctionalRoleMemberRequest
from ..model.batch_create_functional_role_member_response import BatchCreateFunctionalRoleMemberResponse as BatchCreateFunctionalRoleMemberResponse
from ..model.batch_delete_functional_role_member_request import BatchDeleteFunctionalRoleMemberRequest as BatchDeleteFunctionalRoleMemberRequest
from ..model.batch_delete_functional_role_member_response import BatchDeleteFunctionalRoleMemberResponse as BatchDeleteFunctionalRoleMemberResponse
from ..model.get_functional_role_member_request import GetFunctionalRoleMemberRequest as GetFunctionalRoleMemberRequest
from ..model.get_functional_role_member_response import GetFunctionalRoleMemberResponse as GetFunctionalRoleMemberResponse
from ..model.list_functional_role_member_request import ListFunctionalRoleMemberRequest as ListFunctionalRoleMemberRequest
from ..model.list_functional_role_member_response import ListFunctionalRoleMemberResponse as ListFunctionalRoleMemberResponse
from ..model.scopes_functional_role_member_request import ScopesFunctionalRoleMemberRequest as ScopesFunctionalRoleMemberRequest
from ..model.scopes_functional_role_member_response import ScopesFunctionalRoleMemberResponse as ScopesFunctionalRoleMemberResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class FunctionalRoleMember:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_create(self, request: BatchCreateFunctionalRoleMemberRequest, option: RequestOption | None = None) -> BatchCreateFunctionalRoleMemberResponse: ...
    async def abatch_create(self, request: BatchCreateFunctionalRoleMemberRequest, option: RequestOption | None = None) -> BatchCreateFunctionalRoleMemberResponse: ...
    def batch_delete(self, request: BatchDeleteFunctionalRoleMemberRequest, option: RequestOption | None = None) -> BatchDeleteFunctionalRoleMemberResponse: ...
    async def abatch_delete(self, request: BatchDeleteFunctionalRoleMemberRequest, option: RequestOption | None = None) -> BatchDeleteFunctionalRoleMemberResponse: ...
    def get(self, request: GetFunctionalRoleMemberRequest, option: RequestOption | None = None) -> GetFunctionalRoleMemberResponse: ...
    async def aget(self, request: GetFunctionalRoleMemberRequest, option: RequestOption | None = None) -> GetFunctionalRoleMemberResponse: ...
    def list(self, request: ListFunctionalRoleMemberRequest, option: RequestOption | None = None) -> ListFunctionalRoleMemberResponse: ...
    async def alist(self, request: ListFunctionalRoleMemberRequest, option: RequestOption | None = None) -> ListFunctionalRoleMemberResponse: ...
    def scopes(self, request: ScopesFunctionalRoleMemberRequest, option: RequestOption | None = None) -> ScopesFunctionalRoleMemberResponse: ...
    async def ascopes(self, request: ScopesFunctionalRoleMemberRequest, option: RequestOption | None = None) -> ScopesFunctionalRoleMemberResponse: ...
