from .get_faq_response_body import GetFaqResponseBody as GetFaqResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetFaqResponse(BaseResponse):
    data: GetFaqResponseBody | None
    def __init__(self, d=None) -> None: ...
