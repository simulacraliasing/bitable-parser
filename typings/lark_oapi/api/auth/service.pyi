from .v3.version import V3 as V3
from lark_oapi.core.model import Config as Config

class AuthService:
    v3: V3
    def __init__(self, config: Config) -> None: ...
