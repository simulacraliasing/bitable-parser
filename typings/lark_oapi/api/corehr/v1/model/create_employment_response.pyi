from .create_employment_response_body import CreateEmploymentResponseBody as CreateEmploymentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateEmploymentResponse(BaseResponse):
    data: CreateEmploymentResponseBody | None
    def __init__(self, d=None) -> None: ...
