from .upload_person_response_body import UploadPersonResponseBody as UploadPersonResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadPersonResponse(BaseResponse):
    data: UploadPersonResponseBody | None
    def __init__(self, d=None) -> None: ...
