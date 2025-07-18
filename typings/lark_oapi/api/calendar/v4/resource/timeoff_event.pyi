from ..model.create_timeoff_event_request import CreateTimeoffEventRequest as CreateTimeoffEventRequest
from ..model.create_timeoff_event_response import CreateTimeoffEventResponse as CreateTimeoffEventResponse
from ..model.delete_timeoff_event_request import DeleteTimeoffEventRequest as DeleteTimeoffEventRequest
from ..model.delete_timeoff_event_response import DeleteTimeoffEventResponse as DeleteTimeoffEventResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class TimeoffEvent:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateTimeoffEventRequest, option: RequestOption | None = None) -> CreateTimeoffEventResponse: ...
    async def acreate(self, request: CreateTimeoffEventRequest, option: RequestOption | None = None) -> CreateTimeoffEventResponse: ...
    def delete(self, request: DeleteTimeoffEventRequest, option: RequestOption | None = None) -> DeleteTimeoffEventResponse: ...
    async def adelete(self, request: DeleteTimeoffEventRequest, option: RequestOption | None = None) -> DeleteTimeoffEventResponse: ...
