from ..model.create_entity_request import CreateEntityRequest as CreateEntityRequest
from ..model.create_entity_response import CreateEntityResponse as CreateEntityResponse
from ..model.update_entity_request import UpdateEntityRequest as UpdateEntityRequest
from ..model.update_entity_response import UpdateEntityResponse as UpdateEntityResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Entity:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateEntityRequest, option: RequestOption | None = None) -> CreateEntityResponse: ...
    async def acreate(self, request: CreateEntityRequest, option: RequestOption | None = None) -> CreateEntityResponse: ...
    def update(self, request: UpdateEntityRequest, option: RequestOption | None = None) -> UpdateEntityResponse: ...
    async def aupdate(self, request: UpdateEntityRequest, option: RequestOption | None = None) -> UpdateEntityResponse: ...
