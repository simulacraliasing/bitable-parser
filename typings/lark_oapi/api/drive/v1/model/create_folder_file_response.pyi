from .create_folder_file_response_body import CreateFolderFileResponseBody as CreateFolderFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateFolderFileResponse(BaseResponse):
    data: CreateFolderFileResponseBody | None
    def __init__(self, d=None) -> None: ...
