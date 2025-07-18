from ..model.add_managers_chat_managers_request import AddManagersChatManagersRequest as AddManagersChatManagersRequest
from ..model.add_managers_chat_managers_response import AddManagersChatManagersResponse as AddManagersChatManagersResponse
from ..model.delete_managers_chat_managers_request import DeleteManagersChatManagersRequest as DeleteManagersChatManagersRequest
from ..model.delete_managers_chat_managers_response import DeleteManagersChatManagersResponse as DeleteManagersChatManagersResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ChatManagers:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def add_managers(self, request: AddManagersChatManagersRequest, option: RequestOption | None = None) -> AddManagersChatManagersResponse: ...
    async def aadd_managers(self, request: AddManagersChatManagersRequest, option: RequestOption | None = None) -> AddManagersChatManagersResponse: ...
    def delete_managers(self, request: DeleteManagersChatManagersRequest, option: RequestOption | None = None) -> DeleteManagersChatManagersResponse: ...
    async def adelete_managers(self, request: DeleteManagersChatManagersRequest, option: RequestOption | None = None) -> DeleteManagersChatManagersResponse: ...
