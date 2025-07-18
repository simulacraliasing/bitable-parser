from .create_talent_external_info_response_body import CreateTalentExternalInfoResponseBody as CreateTalentExternalInfoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTalentExternalInfoResponse(BaseResponse):
    data: CreateTalentExternalInfoResponseBody | None
    def __init__(self, d=None) -> None: ...
