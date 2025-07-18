from ..model.check_external_instance_request import CheckExternalInstanceRequest as CheckExternalInstanceRequest
from ..model.check_external_instance_response import CheckExternalInstanceResponse as CheckExternalInstanceResponse
from ..model.create_external_instance_request import CreateExternalInstanceRequest as CreateExternalInstanceRequest
from ..model.create_external_instance_response import CreateExternalInstanceResponse as CreateExternalInstanceResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ExternalInstance:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def check(self, request: CheckExternalInstanceRequest, option: RequestOption | None = None) -> CheckExternalInstanceResponse: ...
    async def acheck(self, request: CheckExternalInstanceRequest, option: RequestOption | None = None) -> CheckExternalInstanceResponse: ...
    def create(self, request: CreateExternalInstanceRequest, option: RequestOption | None = None) -> CreateExternalInstanceResponse: ...
    async def acreate(self, request: CreateExternalInstanceRequest, option: RequestOption | None = None) -> CreateExternalInstanceResponse: ...
