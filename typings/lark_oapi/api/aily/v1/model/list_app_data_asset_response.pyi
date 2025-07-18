from .list_app_data_asset_response_body import ListAppDataAssetResponseBody as ListAppDataAssetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppDataAssetResponse(BaseResponse):
    data: ListAppDataAssetResponseBody | None
    def __init__(self, d=None) -> None: ...
