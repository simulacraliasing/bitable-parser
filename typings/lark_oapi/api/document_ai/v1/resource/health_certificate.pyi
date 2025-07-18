from ..model.recognize_health_certificate_request import RecognizeHealthCertificateRequest as RecognizeHealthCertificateRequest
from ..model.recognize_health_certificate_response import RecognizeHealthCertificateResponse as RecognizeHealthCertificateResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class HealthCertificate:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def recognize(self, request: RecognizeHealthCertificateRequest, option: RequestOption | None = None) -> RecognizeHealthCertificateResponse: ...
    async def arecognize(self, request: RecognizeHealthCertificateRequest, option: RequestOption | None = None) -> RecognizeHealthCertificateResponse: ...
