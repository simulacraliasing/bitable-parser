from .patch_app_table_view_response_body import PatchAppTableViewResponseBody as PatchAppTableViewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchAppTableViewResponse(BaseResponse):
    data: PatchAppTableViewResponseBody | None
    def __init__(self, d=None) -> None: ...
