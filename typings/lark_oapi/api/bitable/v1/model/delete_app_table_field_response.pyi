from .delete_app_table_field_response_body import DeleteAppTableFieldResponseBody as DeleteAppTableFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteAppTableFieldResponse(BaseResponse):
    data: DeleteAppTableFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
