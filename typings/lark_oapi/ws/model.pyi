from _typeshed import Incomplete
from lark_oapi.core.construct import init as init

class ClientConfig:
    ReconnectCount: int | None
    ReconnectInterval: int | None
    ReconnectNonce: int | None
    PingInterval: int | None
    def __init__(self, d=None) -> None: ...

class Endpoint:
    URL: str | None
    ClientConfig: ClientConfig | None
    def __init__(self, d=None) -> None: ...

class EndpointResp:
    code: int | None
    msg: str | None
    data: Endpoint | None
    def __init__(self, d=None) -> None: ...

class Response:
    code: Incomplete
    headers: Incomplete
    data: Incomplete
    def __init__(self, code: int = None, headers: dict[str, str] = None, data: bytes = None) -> None: ...
