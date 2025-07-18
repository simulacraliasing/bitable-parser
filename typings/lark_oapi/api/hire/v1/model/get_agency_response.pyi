from .get_agency_response_body import GetAgencyResponseBody as GetAgencyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAgencyResponse(BaseResponse):
    data: GetAgencyResponseBody | None
    def __init__(self, d=None) -> None: ...
