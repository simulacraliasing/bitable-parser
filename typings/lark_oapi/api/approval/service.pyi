from .v4.version import V4 as V4
from lark_oapi.core.model import Config as Config

class ApprovalService:
    v4: V4
    def __init__(self, config: Config) -> None: ...
