from ..model.get_by_application_referral_request import GetByApplicationReferralRequest as GetByApplicationReferralRequest
from ..model.get_by_application_referral_response import GetByApplicationReferralResponse as GetByApplicationReferralResponse
from ..model.search_referral_request import SearchReferralRequest as SearchReferralRequest
from ..model.search_referral_response import SearchReferralResponse as SearchReferralResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Referral:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get_by_application(self, request: GetByApplicationReferralRequest, option: RequestOption | None = None) -> GetByApplicationReferralResponse: ...
    async def aget_by_application(self, request: GetByApplicationReferralRequest, option: RequestOption | None = None) -> GetByApplicationReferralResponse: ...
    def search(self, request: SearchReferralRequest, option: RequestOption | None = None) -> SearchReferralResponse: ...
    async def asearch(self, request: SearchReferralRequest, option: RequestOption | None = None) -> SearchReferralResponse: ...
