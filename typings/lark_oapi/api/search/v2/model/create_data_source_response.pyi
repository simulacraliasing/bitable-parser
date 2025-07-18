from .create_data_source_response_body import CreateDataSourceResponseBody as CreateDataSourceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateDataSourceResponse(BaseResponse):
    data: CreateDataSourceResponseBody | None
    def __init__(self, d=None) -> None: ...
