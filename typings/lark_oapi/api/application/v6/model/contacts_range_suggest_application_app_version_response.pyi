from .contacts_range_suggest_application_app_version_response_body import ContactsRangeSuggestApplicationAppVersionResponseBody as ContactsRangeSuggestApplicationAppVersionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ContactsRangeSuggestApplicationAppVersionResponse(BaseResponse):
    data: ContactsRangeSuggestApplicationAppVersionResponseBody | None
    def __init__(self, d=None) -> None: ...
