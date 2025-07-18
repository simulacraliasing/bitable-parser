from .get_app_data_asset_response_body import GetAppDataAssetResponseBody as GetAppDataAssetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAppDataAssetResponse(BaseResponse):
    data: GetAppDataAssetResponseBody | None
    def __init__(self, d=None) -> None: ...
