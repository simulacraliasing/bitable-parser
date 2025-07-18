from .list_interview_registration_schema_response_body import ListInterviewRegistrationSchemaResponseBody as ListInterviewRegistrationSchemaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListInterviewRegistrationSchemaResponse(BaseResponse):
    data: ListInterviewRegistrationSchemaResponseBody | None
    def __init__(self, d=None) -> None: ...
