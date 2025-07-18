from .list_national_id_type_response_body import ListNationalIdTypeResponseBody as ListNationalIdTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListNationalIdTypeResponse(BaseResponse):
    data: ListNationalIdTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
