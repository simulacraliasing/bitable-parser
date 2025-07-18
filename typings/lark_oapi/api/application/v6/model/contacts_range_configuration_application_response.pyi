from .contacts_range_configuration_application_response_body import ContactsRangeConfigurationApplicationResponseBody as ContactsRangeConfigurationApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ContactsRangeConfigurationApplicationResponse(BaseResponse):
    data: ContactsRangeConfigurationApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
