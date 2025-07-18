from ..model.create_rule_external_request import CreateRuleExternalRequest as CreateRuleExternalRequest
from ..model.create_rule_external_response import CreateRuleExternalResponse as CreateRuleExternalResponse
from ..model.delete_rule_external_request import DeleteRuleExternalRequest as DeleteRuleExternalRequest
from ..model.delete_rule_external_response import DeleteRuleExternalResponse as DeleteRuleExternalResponse
from ..model.device_bind_rule_external_request import DeviceBindRuleExternalRequest as DeviceBindRuleExternalRequest
from ..model.device_bind_rule_external_response import DeviceBindRuleExternalResponse as DeviceBindRuleExternalResponse
from ..model.get_rule_external_request import GetRuleExternalRequest as GetRuleExternalRequest
from ..model.get_rule_external_response import GetRuleExternalResponse as GetRuleExternalResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class RuleExternal:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateRuleExternalRequest, option: RequestOption | None = None) -> CreateRuleExternalResponse: ...
    async def acreate(self, request: CreateRuleExternalRequest, option: RequestOption | None = None) -> CreateRuleExternalResponse: ...
    def delete(self, request: DeleteRuleExternalRequest, option: RequestOption | None = None) -> DeleteRuleExternalResponse: ...
    async def adelete(self, request: DeleteRuleExternalRequest, option: RequestOption | None = None) -> DeleteRuleExternalResponse: ...
    def device_bind(self, request: DeviceBindRuleExternalRequest, option: RequestOption | None = None) -> DeviceBindRuleExternalResponse: ...
    async def adevice_bind(self, request: DeviceBindRuleExternalRequest, option: RequestOption | None = None) -> DeviceBindRuleExternalResponse: ...
    def get(self, request: GetRuleExternalRequest, option: RequestOption | None = None) -> GetRuleExternalResponse: ...
    async def aget(self, request: GetRuleExternalRequest, option: RequestOption | None = None) -> GetRuleExternalResponse: ...
