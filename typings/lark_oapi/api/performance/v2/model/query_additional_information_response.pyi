from .query_additional_information_response_body import QueryAdditionalInformationResponseBody as QueryAdditionalInformationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryAdditionalInformationResponse(BaseResponse):
    data: QueryAdditionalInformationResponseBody | None
    def __init__(self, d=None) -> None: ...
