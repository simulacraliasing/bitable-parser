from .create_by_resume_website_delivery_response_body import CreateByResumeWebsiteDeliveryResponseBody as CreateByResumeWebsiteDeliveryResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateByResumeWebsiteDeliveryResponse(BaseResponse):
    data: CreateByResumeWebsiteDeliveryResponseBody | None
    def __init__(self, d=None) -> None: ...
