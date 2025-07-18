from ..model.create_ticket_customized_field_request import CreateTicketCustomizedFieldRequest as CreateTicketCustomizedFieldRequest
from ..model.create_ticket_customized_field_response import CreateTicketCustomizedFieldResponse as CreateTicketCustomizedFieldResponse
from ..model.delete_ticket_customized_field_request import DeleteTicketCustomizedFieldRequest as DeleteTicketCustomizedFieldRequest
from ..model.delete_ticket_customized_field_response import DeleteTicketCustomizedFieldResponse as DeleteTicketCustomizedFieldResponse
from ..model.get_ticket_customized_field_request import GetTicketCustomizedFieldRequest as GetTicketCustomizedFieldRequest
from ..model.get_ticket_customized_field_response import GetTicketCustomizedFieldResponse as GetTicketCustomizedFieldResponse
from ..model.list_ticket_customized_field_request import ListTicketCustomizedFieldRequest as ListTicketCustomizedFieldRequest
from ..model.list_ticket_customized_field_response import ListTicketCustomizedFieldResponse as ListTicketCustomizedFieldResponse
from ..model.patch_ticket_customized_field_request import PatchTicketCustomizedFieldRequest as PatchTicketCustomizedFieldRequest
from ..model.patch_ticket_customized_field_response import PatchTicketCustomizedFieldResponse as PatchTicketCustomizedFieldResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class TicketCustomizedField:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateTicketCustomizedFieldRequest, option: RequestOption | None = None) -> CreateTicketCustomizedFieldResponse: ...
    async def acreate(self, request: CreateTicketCustomizedFieldRequest, option: RequestOption | None = None) -> CreateTicketCustomizedFieldResponse: ...
    def delete(self, request: DeleteTicketCustomizedFieldRequest, option: RequestOption | None = None) -> DeleteTicketCustomizedFieldResponse: ...
    async def adelete(self, request: DeleteTicketCustomizedFieldRequest, option: RequestOption | None = None) -> DeleteTicketCustomizedFieldResponse: ...
    def get(self, request: GetTicketCustomizedFieldRequest, option: RequestOption | None = None) -> GetTicketCustomizedFieldResponse: ...
    async def aget(self, request: GetTicketCustomizedFieldRequest, option: RequestOption | None = None) -> GetTicketCustomizedFieldResponse: ...
    def list(self, request: ListTicketCustomizedFieldRequest, option: RequestOption | None = None) -> ListTicketCustomizedFieldResponse: ...
    async def alist(self, request: ListTicketCustomizedFieldRequest, option: RequestOption | None = None) -> ListTicketCustomizedFieldResponse: ...
    def patch(self, request: PatchTicketCustomizedFieldRequest, option: RequestOption | None = None) -> PatchTicketCustomizedFieldResponse: ...
    async def apatch(self, request: PatchTicketCustomizedFieldRequest, option: RequestOption | None = None) -> PatchTicketCustomizedFieldResponse: ...
