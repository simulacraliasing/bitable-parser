from ..model.create_chat_request import CreateChatRequest as CreateChatRequest
from ..model.create_chat_response import CreateChatResponse as CreateChatResponse
from ..model.delete_chat_request import DeleteChatRequest as DeleteChatRequest
from ..model.delete_chat_response import DeleteChatResponse as DeleteChatResponse
from ..model.get_chat_request import GetChatRequest as GetChatRequest
from ..model.get_chat_response import GetChatResponse as GetChatResponse
from ..model.link_chat_request import LinkChatRequest as LinkChatRequest
from ..model.link_chat_response import LinkChatResponse as LinkChatResponse
from ..model.list_chat_request import ListChatRequest as ListChatRequest
from ..model.list_chat_response import ListChatResponse as ListChatResponse
from ..model.search_chat_request import SearchChatRequest as SearchChatRequest
from ..model.search_chat_response import SearchChatResponse as SearchChatResponse
from ..model.update_chat_request import UpdateChatRequest as UpdateChatRequest
from ..model.update_chat_response import UpdateChatResponse as UpdateChatResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Chat:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateChatRequest, option: RequestOption | None = None) -> CreateChatResponse: ...
    async def acreate(self, request: CreateChatRequest, option: RequestOption | None = None) -> CreateChatResponse: ...
    def delete(self, request: DeleteChatRequest, option: RequestOption | None = None) -> DeleteChatResponse: ...
    async def adelete(self, request: DeleteChatRequest, option: RequestOption | None = None) -> DeleteChatResponse: ...
    def get(self, request: GetChatRequest, option: RequestOption | None = None) -> GetChatResponse: ...
    async def aget(self, request: GetChatRequest, option: RequestOption | None = None) -> GetChatResponse: ...
    def link(self, request: LinkChatRequest, option: RequestOption | None = None) -> LinkChatResponse: ...
    async def alink(self, request: LinkChatRequest, option: RequestOption | None = None) -> LinkChatResponse: ...
    def list(self, request: ListChatRequest, option: RequestOption | None = None) -> ListChatResponse: ...
    async def alist(self, request: ListChatRequest, option: RequestOption | None = None) -> ListChatResponse: ...
    def search(self, request: SearchChatRequest, option: RequestOption | None = None) -> SearchChatResponse: ...
    async def asearch(self, request: SearchChatRequest, option: RequestOption | None = None) -> SearchChatResponse: ...
    def update(self, request: UpdateChatRequest, option: RequestOption | None = None) -> UpdateChatResponse: ...
    async def aupdate(self, request: UpdateChatRequest, option: RequestOption | None = None) -> UpdateChatResponse: ...
