from .v6.version import V6 as V6
from lark_oapi.core.model import Config as Config

class ApplicationService:
    v6: V6
    def __init__(self, config: Config) -> None: ...
