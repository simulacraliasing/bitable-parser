from ..model.bind_user_auth_data_relation_request import BindUserAuthDataRelationRequest as BindUserAuthDataRelationRequest
from ..model.bind_user_auth_data_relation_response import BindUserAuthDataRelationResponse as BindUserAuthDataRelationResponse
from ..model.unbind_user_auth_data_relation_request import UnbindUserAuthDataRelationRequest as UnbindUserAuthDataRelationRequest
from ..model.unbind_user_auth_data_relation_response import UnbindUserAuthDataRelationResponse as UnbindUserAuthDataRelationResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class UserAuthDataRelation:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def bind(self, request: BindUserAuthDataRelationRequest, option: RequestOption | None = None) -> BindUserAuthDataRelationResponse: ...
    async def abind(self, request: BindUserAuthDataRelationRequest, option: RequestOption | None = None) -> BindUserAuthDataRelationResponse: ...
    def unbind(self, request: UnbindUserAuthDataRelationRequest, option: RequestOption | None = None) -> UnbindUserAuthDataRelationResponse: ...
    async def aunbind(self, request: UnbindUserAuthDataRelationRequest, option: RequestOption | None = None) -> UnbindUserAuthDataRelationResponse: ...
