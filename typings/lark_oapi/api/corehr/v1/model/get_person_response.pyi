from .get_person_response_body import GetPersonResponseBody as GetPersonResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetPersonResponse(BaseResponse):
    data: GetPersonResponseBody | None
    def __init__(self, d=None) -> None: ...
