from .get_website_delivery_task_response_body import GetWebsiteDeliveryTaskResponseBody as GetWebsiteDeliveryTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetWebsiteDeliveryTaskResponse(BaseResponse):
    data: GetWebsiteDeliveryTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
