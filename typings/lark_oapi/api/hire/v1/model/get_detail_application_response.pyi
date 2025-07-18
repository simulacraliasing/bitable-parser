from .get_detail_application_response_body import GetDetailApplicationResponseBody as GetDetailApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetDetailApplicationResponse(BaseResponse):
    data: GetDetailApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
