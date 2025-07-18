from .get_export_response_body import GetExportResponseBody as GetExportResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetExportResponse(BaseResponse):
    data: GetExportResponseBody | None
    def __init__(self, d=None) -> None: ...
