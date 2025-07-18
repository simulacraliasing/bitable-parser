from .add_to_folder_talent_response_body import AddToFolderTalentResponseBody as AddToFolderTalentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AddToFolderTalentResponse(BaseResponse):
    data: AddToFolderTalentResponseBody | None
    def __init__(self, d=None) -> None: ...
