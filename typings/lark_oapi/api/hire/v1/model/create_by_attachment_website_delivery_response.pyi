from .create_by_attachment_website_delivery_response_body import CreateByAttachmentWebsiteDeliveryResponseBody as CreateByAttachmentWebsiteDeliveryResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateByAttachmentWebsiteDeliveryResponse(BaseResponse):
    data: CreateByAttachmentWebsiteDeliveryResponseBody | None
    def __init__(self, d=None) -> None: ...
