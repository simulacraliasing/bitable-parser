from .list_task_collaborator_response_body import ListTaskCollaboratorResponseBody as ListTaskCollaboratorResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTaskCollaboratorResponse(BaseResponse):
    data: ListTaskCollaboratorResponseBody | None
    def __init__(self, d=None) -> None: ...
