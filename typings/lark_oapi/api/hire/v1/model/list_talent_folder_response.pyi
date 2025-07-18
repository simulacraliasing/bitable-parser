from .list_talent_folder_response_body import ListTalentFolderResponseBody as ListTalentFolderResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTalentFolderResponse(BaseResponse):
    data: ListTalentFolderResponseBody | None
    def __init__(self, d=None) -> None: ...
