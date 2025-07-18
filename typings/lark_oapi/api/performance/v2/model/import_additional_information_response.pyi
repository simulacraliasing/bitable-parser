from .import_additional_information_response_body import ImportAdditionalInformationResponseBody as ImportAdditionalInformationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ImportAdditionalInformationResponse(BaseResponse):
    data: ImportAdditionalInformationResponseBody | None
    def __init__(self, d=None) -> None: ...
