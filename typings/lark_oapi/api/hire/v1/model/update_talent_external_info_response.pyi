from .update_talent_external_info_response_body import UpdateTalentExternalInfoResponseBody as UpdateTalentExternalInfoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateTalentExternalInfoResponse(BaseResponse):
    data: UpdateTalentExternalInfoResponseBody | None
    def __init__(self, d=None) -> None: ...
