from ..model.subscribe_event_request import SubscribeEventRequest as SubscribeEventRequest
from ..model.subscribe_event_response import SubscribeEventResponse as SubscribeEventResponse
from ..model.unsubscribe_event_request import UnsubscribeEventRequest as UnsubscribeEventRequest
from ..model.unsubscribe_event_response import UnsubscribeEventResponse as UnsubscribeEventResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Event:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def subscribe(self, request: SubscribeEventRequest, option: RequestOption | None = None) -> SubscribeEventResponse: ...
    async def asubscribe(self, request: SubscribeEventRequest, option: RequestOption | None = None) -> SubscribeEventResponse: ...
    def unsubscribe(self, request: UnsubscribeEventRequest, option: RequestOption | None = None) -> UnsubscribeEventResponse: ...
    async def aunsubscribe(self, request: UnsubscribeEventRequest, option: RequestOption | None = None) -> UnsubscribeEventResponse: ...
