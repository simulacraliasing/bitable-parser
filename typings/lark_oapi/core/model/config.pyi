from lark_oapi.core import AppType as AppType, LogLevel as LogLevel
from lark_oapi.core.cache import ICache as ICache
from lark_oapi.core.const import FEISHU_DOMAIN as FEISHU_DOMAIN

class Config:
    app_id: str | None
    app_secret: str | None
    domain: str
    timeout: float | None
    app_type: AppType
    enable_set_token: bool
    cache: ICache | None
    log_level: LogLevel
    def __init__(self) -> None: ...
