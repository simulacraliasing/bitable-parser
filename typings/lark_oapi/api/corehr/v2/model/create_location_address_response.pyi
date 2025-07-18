from .create_location_address_response_body import CreateLocationAddressResponseBody as CreateLocationAddressResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateLocationAddressResponse(BaseResponse):
    data: CreateLocationAddressResponseBody | None
    def __init__(self, d=None) -> None: ...
