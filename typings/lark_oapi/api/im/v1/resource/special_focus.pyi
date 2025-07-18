from typing import *
from ..model.list_special_focus_request import ListSpecialFocusRequest as ListSpecialFocusRequest
from ..model.list_special_focus_response import ListSpecialFocusResponse as ListSpecialFocusResponse
from ..model.unread_special_focus_request import UnreadSpecialFocusRequest as UnreadSpecialFocusRequest
from ..model.unread_special_focus_response import UnreadSpecialFocusResponse as UnreadSpecialFocusResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify

class SpecialFocus:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListSpecialFocusRequest, option: Optional[RequestOption] = None) -> ListSpecialFocusResponse: ...
    def unread(self, request: UnreadSpecialFocusRequest, option: Optional[RequestOption] = None) -> UnreadSpecialFocusResponse: ...
