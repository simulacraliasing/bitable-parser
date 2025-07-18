from .list_referral_website_job_post_response_body import ListReferralWebsiteJobPostResponseBody as ListReferralWebsiteJobPostResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListReferralWebsiteJobPostResponse(BaseResponse):
    data: ListReferralWebsiteJobPostResponseBody | None
    def __init__(self, d=None) -> None: ...
