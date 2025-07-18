from ..model.archive_payment_activity_request import ArchivePaymentActivityRequest as ArchivePaymentActivityRequest
from ..model.archive_payment_activity_response import ArchivePaymentActivityResponse as ArchivePaymentActivityResponse
from ..model.list_payment_activity_request import ListPaymentActivityRequest as ListPaymentActivityRequest
from ..model.list_payment_activity_response import ListPaymentActivityResponse as ListPaymentActivityResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class PaymentActivity:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def archive(self, request: ArchivePaymentActivityRequest, option: RequestOption | None = None) -> ArchivePaymentActivityResponse: ...
    async def aarchive(self, request: ArchivePaymentActivityRequest, option: RequestOption | None = None) -> ArchivePaymentActivityResponse: ...
    def list(self, request: ListPaymentActivityRequest, option: RequestOption | None = None) -> ListPaymentActivityResponse: ...
    async def alist(self, request: ListPaymentActivityRequest, option: RequestOption | None = None) -> ListPaymentActivityResponse: ...
