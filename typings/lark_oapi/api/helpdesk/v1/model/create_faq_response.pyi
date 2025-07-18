from .create_faq_response_body import CreateFaqResponseBody as CreateFaqResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateFaqResponse(BaseResponse):
    data: CreateFaqResponseBody | None
    def __init__(self, d=None) -> None: ...
