from .delete_app_data_asset_response_body import DeleteAppDataAssetResponseBody as DeleteAppDataAssetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteAppDataAssetResponse(BaseResponse):
    data: DeleteAppDataAssetResponseBody | None
    def __init__(self, d=None) -> None: ...
