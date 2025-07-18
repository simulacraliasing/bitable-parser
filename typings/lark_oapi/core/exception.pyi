from _typeshed import Incomplete

class NoAuthorizationException(Exception):
    msg: str
    def __init__(self, msg: str) -> None: ...

class ObtainAccessTokenException(Exception):
    desc: Incomplete
    code: Incomplete
    msg: Incomplete
    def __init__(self, desc: str, code: int, msg: str) -> None: ...

class UnmarshalException(Exception):
    dst: Incomplete
    src: Incomplete
    field: Incomplete
    def __init__(self, dst, src, field) -> None: ...

class InvalidArgsException(Exception):
    msg: str
    def __init__(self, msg: str) -> None: ...

class AccessDeniedException(Exception):
    msg: str
    def __init__(self, msg: str) -> None: ...

class EventException(Exception):
    msg: str
    def __init__(self, msg: str) -> None: ...

class CardException(Exception):
    msg: str
    def __init__(self, msg: str) -> None: ...
