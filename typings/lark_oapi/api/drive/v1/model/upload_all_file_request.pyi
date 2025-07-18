from .upload_all_file_request_body import UploadAllFileRequestBody as UploadAllFileRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class UploadAllFileRequest(BaseRequest):
    request_body: UploadAllFileRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> UploadAllFileRequestBuilder: ...

class UploadAllFileRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: UploadAllFileRequestBody) -> UploadAllFileRequestBuilder: ...
    def build(self) -> UploadAllFileRequest: ...
