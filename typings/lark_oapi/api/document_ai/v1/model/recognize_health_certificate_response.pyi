from .recognize_health_certificate_response_body import RecognizeHealthCertificateResponseBody as RecognizeHealthCertificateResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeHealthCertificateResponse(BaseResponse):
    data: RecognizeHealthCertificateResponseBody | None
    def __init__(self, d=None) -> None: ...
