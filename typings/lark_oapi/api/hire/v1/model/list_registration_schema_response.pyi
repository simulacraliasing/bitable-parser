from .list_registration_schema_response_body import ListRegistrationSchemaResponseBody as ListRegistrationSchemaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListRegistrationSchemaResponse(BaseResponse):
    data: ListRegistrationSchemaResponseBody | None
    def __init__(self, d=None) -> None: ...
