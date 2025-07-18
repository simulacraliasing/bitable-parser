from .protect_search_agency_response_body import ProtectSearchAgencyResponseBody as ProtectSearchAgencyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ProtectSearchAgencyResponse(BaseResponse):
    data: ProtectSearchAgencyResponseBody | None
    def __init__(self, d=None) -> None: ...
