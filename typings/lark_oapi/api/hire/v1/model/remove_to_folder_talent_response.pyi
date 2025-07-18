from .remove_to_folder_talent_response_body import RemoveToFolderTalentResponseBody as RemoveToFolderTalentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RemoveToFolderTalentResponse(BaseResponse):
    data: RemoveToFolderTalentResponseBody | None
    def __init__(self, d=None) -> None: ...
