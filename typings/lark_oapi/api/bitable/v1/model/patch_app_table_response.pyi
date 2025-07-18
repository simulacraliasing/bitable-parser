from .patch_app_table_response_body import PatchAppTableResponseBody as PatchAppTableResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchAppTableResponse(BaseResponse):
    data: PatchAppTableResponseBody | None
    def __init__(self, d=None) -> None: ...
