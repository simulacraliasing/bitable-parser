from .list_outbound_ip_response_body import ListOutboundIpResponseBody as ListOutboundIpResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListOutboundIpResponse(BaseResponse):
    data: ListOutboundIpResponseBody | None
    def __init__(self, d=None) -> None: ...
