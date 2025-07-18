from .v2.version import V2 as V2
from lark_oapi.core.model import Config as Config

class TenantService:
    v2: V2
    def __init__(self, config: Config) -> None: ...
