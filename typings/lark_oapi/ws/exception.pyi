from _typeshed import Incomplete

class ClientException(Exception):
    code: Incomplete
    def __init__(self, code: int, msg: str) -> None: ...

class ServerException(Exception):
    code: Incomplete
    def __init__(self, code: int, msg: str) -> None: ...

class HeaderNotFoundException(Exception):
    key: Incomplete
    def __init__(self, key: str) -> None: ...

class ConnectionClosedException(Exception):
    def __init__(self, msg: str) -> None: ...

class ServerUnreachableException(Exception):
    def __init__(self, msg: str) -> None: ...
