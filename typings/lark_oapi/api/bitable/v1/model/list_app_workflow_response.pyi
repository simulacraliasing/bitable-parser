from .list_app_workflow_response_body import ListAppWorkflowResponseBody as ListAppWorkflowResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppWorkflowResponse(BaseResponse):
    data: ListAppWorkflowResponseBody | None
    def __init__(self, d=None) -> None: ...
