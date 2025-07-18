from .get_referral_website_job_post_response_body import GetReferralWebsiteJobPostResponseBody as GetReferralWebsiteJobPostResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetReferralWebsiteJobPostResponse(BaseResponse):
    data: GetReferralWebsiteJobPostResponseBody | None
    def __init__(self, d=None) -> None: ...
