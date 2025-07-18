from .list_website_job_post_response_body import ListWebsiteJobPostResponseBody as ListWebsiteJobPostResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListWebsiteJobPostResponse(BaseResponse):
    data: ListWebsiteJobPostResponseBody | None
    def __init__(self, d=None) -> None: ...
