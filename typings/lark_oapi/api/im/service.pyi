from .v1.version import V1 as V1
from .v2.version import V2 as V2
from lark_oapi.core.model import Config as Config

class ImService:
    v1: V1
    v2: V2
    def __init__(self, config: Config) -> None: ...
