from ..model.create_visitor_request import CreateVisitorRequest as CreateVisitorRequest
from ..model.create_visitor_response import CreateVisitorResponse as CreateVisitorResponse
from ..model.delete_visitor_request import DeleteVisitorRequest as DeleteVisitorRequest
from ..model.delete_visitor_response import DeleteVisitorResponse as DeleteVisitorResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Visitor:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateVisitorRequest, option: RequestOption | None = None) -> CreateVisitorResponse: ...
    async def acreate(self, request: CreateVisitorRequest, option: RequestOption | None = None) -> CreateVisitorResponse: ...
    def delete(self, request: DeleteVisitorRequest, option: RequestOption | None = None) -> DeleteVisitorResponse: ...
    async def adelete(self, request: DeleteVisitorRequest, option: RequestOption | None = None) -> DeleteVisitorResponse: ...
