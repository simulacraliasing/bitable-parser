from .website_delivery_attachment import WebsiteDeliveryAttachment as WebsiteDeliveryAttachment
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateByAttachmentWebsiteDeliveryRequest(BaseRequest):
    website_id: str | None
    request_body: WebsiteDeliveryAttachment | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateByAttachmentWebsiteDeliveryRequestBuilder: ...

class CreateByAttachmentWebsiteDeliveryRequestBuilder:
    def __init__(self) -> None: ...
    def website_id(self, website_id: str) -> CreateByAttachmentWebsiteDeliveryRequestBuilder: ...
    def request_body(self, request_body: WebsiteDeliveryAttachment) -> CreateByAttachmentWebsiteDeliveryRequestBuilder: ...
    def build(self) -> CreateByAttachmentWebsiteDeliveryRequest: ...
