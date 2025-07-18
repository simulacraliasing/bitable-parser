from .create_shortcut_file_response_body import CreateShortcutFileResponseBody as CreateShortcutFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateShortcutFileResponse(BaseResponse):
    data: CreateShortcutFileResponseBody | None
    def __init__(self, d=None) -> None: ...
