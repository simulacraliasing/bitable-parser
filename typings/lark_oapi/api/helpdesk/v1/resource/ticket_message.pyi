from ..model.create_ticket_message_request import CreateTicketMessageRequest as CreateTicketMessageRequest
from ..model.create_ticket_message_response import CreateTicketMessageResponse as CreateTicketMessageResponse
from ..model.list_ticket_message_request import ListTicketMessageRequest as ListTicketMessageRequest
from ..model.list_ticket_message_response import ListTicketMessageResponse as ListTicketMessageResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class TicketMessage:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateTicketMessageRequest, option: RequestOption | None = None) -> CreateTicketMessageResponse: ...
    async def acreate(self, request: CreateTicketMessageRequest, option: RequestOption | None = None) -> CreateTicketMessageResponse: ...
    def list(self, request: ListTicketMessageRequest, option: RequestOption | None = None) -> ListTicketMessageResponse: ...
    async def alist(self, request: ListTicketMessageRequest, option: RequestOption | None = None) -> ListTicketMessageResponse: ...
