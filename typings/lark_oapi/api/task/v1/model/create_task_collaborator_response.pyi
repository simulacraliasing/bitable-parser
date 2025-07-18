from .create_task_collaborator_response_body import CreateTaskCollaboratorResponseBody as CreateTaskCollaboratorResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTaskCollaboratorResponse(BaseResponse):
    data: CreateTaskCollaboratorResponseBody | None
    def __init__(self, d=None) -> None: ...
