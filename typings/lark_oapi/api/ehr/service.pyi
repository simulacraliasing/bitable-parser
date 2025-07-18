from .v1.version import V1 as V1
from lark_oapi.core.model import Config as Config

class EhrService:
    v1: V1
    def __init__(self, config: Config) -> None: ...
