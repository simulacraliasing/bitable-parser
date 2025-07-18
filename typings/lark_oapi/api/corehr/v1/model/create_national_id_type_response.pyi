from .create_national_id_type_response_body import CreateNationalIdTypeResponseBody as CreateNationalIdTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateNationalIdTypeResponse(BaseResponse):
    data: CreateNationalIdTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
