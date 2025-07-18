from .create_app_table_view_response_body import CreateAppTableViewResponseBody as CreateAppTableViewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAppTableViewResponse(BaseResponse):
    data: CreateAppTableViewResponseBody | None
    def __init__(self, d=None) -> None: ...
