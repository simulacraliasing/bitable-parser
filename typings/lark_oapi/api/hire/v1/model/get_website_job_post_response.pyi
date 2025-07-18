from .get_website_job_post_response_body import GetWebsiteJobPostResponseBody as GetWebsiteJobPostResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetWebsiteJobPostResponse(BaseResponse):
    data: GetWebsiteJobPostResponseBody | None
    def __init__(self, d=None) -> None: ...
