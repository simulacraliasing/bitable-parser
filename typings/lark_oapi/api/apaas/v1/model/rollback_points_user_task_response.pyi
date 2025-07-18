from .rollback_points_user_task_response_body import RollbackPointsUserTaskResponseBody as RollbackPointsUserTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RollbackPointsUserTaskResponse(BaseResponse):
    data: RollbackPointsUserTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
