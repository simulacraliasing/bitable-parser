from .list_moto_response_body import ListMotoResponseBody as ListMotoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMotoResponse(BaseResponse):
    data: ListMotoResponseBody | None
    def __init__(self, d=None) -> None: ...
