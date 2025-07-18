from .create_app_data_asset_response_body import CreateAppDataAssetResponseBody as CreateAppDataAssetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAppDataAssetResponse(BaseResponse):
    data: CreateAppDataAssetResponseBody | None
    def __init__(self, d=None) -> None: ...
