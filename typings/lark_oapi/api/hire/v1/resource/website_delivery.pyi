from ..model.create_by_attachment_website_delivery_request import CreateByAttachmentWebsiteDeliveryRequest as CreateByAttachmentWebsiteDeliveryRequest
from ..model.create_by_attachment_website_delivery_response import CreateByAttachmentWebsiteDeliveryResponse as CreateByAttachmentWebsiteDeliveryResponse
from ..model.create_by_resume_website_delivery_request import CreateByResumeWebsiteDeliveryRequest as CreateByResumeWebsiteDeliveryRequest
from ..model.create_by_resume_website_delivery_response import CreateByResumeWebsiteDeliveryResponse as CreateByResumeWebsiteDeliveryResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class WebsiteDelivery:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create_by_attachment(self, request: CreateByAttachmentWebsiteDeliveryRequest, option: RequestOption | None = None) -> CreateByAttachmentWebsiteDeliveryResponse: ...
    async def acreate_by_attachment(self, request: CreateByAttachmentWebsiteDeliveryRequest, option: RequestOption | None = None) -> CreateByAttachmentWebsiteDeliveryResponse: ...
    def create_by_resume(self, request: CreateByResumeWebsiteDeliveryRequest, option: RequestOption | None = None) -> CreateByResumeWebsiteDeliveryResponse: ...
    async def acreate_by_resume(self, request: CreateByResumeWebsiteDeliveryRequest, option: RequestOption | None = None) -> CreateByResumeWebsiteDeliveryResponse: ...
