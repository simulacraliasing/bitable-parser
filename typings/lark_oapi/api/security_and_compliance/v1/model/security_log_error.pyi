from .gw_common import GwCommon as GwCommon
from .gw_request import GwRequest as GwRequest
from .gw_response import GwResponse as GwResponse
from lark_oapi.core.construct import init as init

class SecurityLogError:
    request: GwRequest | None
    response: GwResponse | None
    common: GwCommon | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SecurityLogErrorBuilder: ...

class SecurityLogErrorBuilder:
    def __init__(self) -> None: ...
    def request(self, request: GwRequest) -> SecurityLogErrorBuilder: ...
    def response(self, response: GwResponse) -> SecurityLogErrorBuilder: ...
    def common(self, common: GwCommon) -> SecurityLogErrorBuilder: ...
    def build(self) -> SecurityLogError: ...
