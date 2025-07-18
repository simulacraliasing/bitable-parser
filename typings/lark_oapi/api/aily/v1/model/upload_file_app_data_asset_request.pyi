from .upload_file_app_data_asset_request_body import UploadFileAppDataAssetRequestBody as UploadFileAppDataAssetRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class UploadFileAppDataAssetRequest(BaseRequest):
    tenant_type: str | None
    app_id: str | None
    request_body: UploadFileAppDataAssetRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> UploadFileAppDataAssetRequestBuilder: ...

class UploadFileAppDataAssetRequestBuilder:
    def __init__(self) -> None: ...
    def tenant_type(self, tenant_type: str) -> UploadFileAppDataAssetRequestBuilder: ...
    def app_id(self, app_id: str) -> UploadFileAppDataAssetRequestBuilder: ...
    def request_body(self, request_body: UploadFileAppDataAssetRequestBody) -> UploadFileAppDataAssetRequestBuilder: ...
    def build(self) -> UploadFileAppDataAssetRequest: ...
