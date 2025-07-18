from .get_data_source_item_response_body import GetDataSourceItemResponseBody as GetDataSourceItemResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetDataSourceItemResponse(BaseResponse):
    data: GetDataSourceItemResponseBody | None
    def __init__(self, d=None) -> None: ...
