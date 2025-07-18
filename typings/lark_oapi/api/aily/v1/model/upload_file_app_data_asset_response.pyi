from .upload_file_app_data_asset_response_body import UploadFileAppDataAssetResponseBody as UploadFileAppDataAssetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadFileAppDataAssetResponse(BaseResponse):
    data: UploadFileAppDataAssetResponseBody | None
    def __init__(self, d=None) -> None: ...
