from .delete_external_application_response_body import DeleteExternalApplicationResponseBody as DeleteExternalApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteExternalApplicationResponse(BaseResponse):
    data: DeleteExternalApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
