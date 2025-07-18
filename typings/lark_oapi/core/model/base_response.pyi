from typing import *

from lark_oapi.core.const import X_TT_LOGID as X_TT_LOGID
from lark_oapi.core.construct import init as init

from .error import Error as Error
from .raw_response import RawResponse as RawResponse

class BaseResponse:
    raw: Optional[RawResponse]
    code: Optional[int]
    msg: Optional[str]
    error: Optional[Error]
    def __init__(self, d=None) -> None: ...
    def success(self) -> bool: ...
    def get_log_id(self) -> Optional[str]: ...
    def get_troubleshooter(self) -> Optional[str]: ...
