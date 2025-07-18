from ..model.get_referral_website_job_post_request import GetReferralWebsiteJobPostRequest as GetReferralWebsiteJobPostRequest
from ..model.get_referral_website_job_post_response import GetReferralWebsiteJobPostResponse as GetReferralWebsiteJobPostResponse
from ..model.list_referral_website_job_post_request import ListReferralWebsiteJobPostRequest as ListReferralWebsiteJobPostRequest
from ..model.list_referral_website_job_post_response import ListReferralWebsiteJobPostResponse as ListReferralWebsiteJobPostResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ReferralWebsiteJobPost:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetReferralWebsiteJobPostRequest, option: RequestOption | None = None) -> GetReferralWebsiteJobPostResponse: ...
    async def aget(self, request: GetReferralWebsiteJobPostRequest, option: RequestOption | None = None) -> GetReferralWebsiteJobPostResponse: ...
    def list(self, request: ListReferralWebsiteJobPostRequest, option: RequestOption | None = None) -> ListReferralWebsiteJobPostResponse: ...
    async def alist(self, request: ListReferralWebsiteJobPostRequest, option: RequestOption | None = None) -> ListReferralWebsiteJobPostResponse: ...
