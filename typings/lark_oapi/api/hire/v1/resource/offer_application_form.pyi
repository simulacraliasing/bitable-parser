from ..model.get_offer_application_form_request import GetOfferApplicationFormRequest as GetOfferApplicationFormRequest
from ..model.get_offer_application_form_response import GetOfferApplicationFormResponse as GetOfferApplicationFormResponse
from ..model.list_offer_application_form_request import ListOfferApplicationFormRequest as ListOfferApplicationFormRequest
from ..model.list_offer_application_form_response import ListOfferApplicationFormResponse as ListOfferApplicationFormResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class OfferApplicationForm:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetOfferApplicationFormRequest, option: RequestOption | None = None) -> GetOfferApplicationFormResponse: ...
    async def aget(self, request: GetOfferApplicationFormRequest, option: RequestOption | None = None) -> GetOfferApplicationFormResponse: ...
    def list(self, request: ListOfferApplicationFormRequest, option: RequestOption | None = None) -> ListOfferApplicationFormResponse: ...
    async def alist(self, request: ListOfferApplicationFormRequest, option: RequestOption | None = None) -> ListOfferApplicationFormResponse: ...
