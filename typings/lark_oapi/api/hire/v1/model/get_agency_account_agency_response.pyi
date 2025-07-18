from .get_agency_account_agency_response_body import GetAgencyAccountAgencyResponseBody as GetAgencyAccountAgencyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAgencyAccountAgencyResponse(BaseResponse):
    data: GetAgencyAccountAgencyResponseBody | None
    def __init__(self, d=None) -> None: ...
