from .batch_delete_collaborator_task_response_body import BatchDeleteCollaboratorTaskResponseBody as BatchDeleteCollaboratorTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchDeleteCollaboratorTaskResponse(BaseResponse):
    data: BatchDeleteCollaboratorTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
