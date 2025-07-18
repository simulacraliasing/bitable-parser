from .get_national_id_type_response_body import GetNationalIdTypeResponseBody as GetNationalIdTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetNationalIdTypeResponse(BaseResponse):
    data: GetNationalIdTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
