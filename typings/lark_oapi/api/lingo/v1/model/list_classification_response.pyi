from .list_classification_response_body import ListClassificationResponseBody as ListClassificationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListClassificationResponse(BaseResponse):
    data: ListClassificationResponseBody | None
    def __init__(self, d=None) -> None: ...
