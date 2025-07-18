from .patch_data_source_response_body import PatchDataSourceResponseBody as PatchDataSourceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchDataSourceResponse(BaseResponse):
    data: PatchDataSourceResponseBody | None
    def __init__(self, d=None) -> None: ...
