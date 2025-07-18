from .transfer_onboard_application_response_body import TransferOnboardApplicationResponseBody as TransferOnboardApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class TransferOnboardApplicationResponse(BaseResponse):
    data: TransferOnboardApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
