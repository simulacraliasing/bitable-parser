from typing import *

class RawRequest:
    uri: Optional[str]
    headers: Dict[str, str]
    body: Optional[bytes]
    def __init__(self) -> None: ...
