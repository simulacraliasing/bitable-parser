from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse
from typing import Any, IO

class TicketImageTicketResponse(BaseResponse):
    file: IO[Any] | None
    file_name: str | None
    def __init__(self, d=None) -> None: ...
