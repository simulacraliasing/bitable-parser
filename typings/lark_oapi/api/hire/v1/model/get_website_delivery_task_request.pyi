from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetWebsiteDeliveryTaskRequest(BaseRequest):
    website_id: str | None
    delivery_task_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetWebsiteDeliveryTaskRequestBuilder: ...

class GetWebsiteDeliveryTaskRequestBuilder:
    def __init__(self) -> None: ...
    def website_id(self, website_id: str) -> GetWebsiteDeliveryTaskRequestBuilder: ...
    def delivery_task_id(self, delivery_task_id: str) -> GetWebsiteDeliveryTaskRequestBuilder: ...
    def build(self) -> GetWebsiteDeliveryTaskRequest: ...
