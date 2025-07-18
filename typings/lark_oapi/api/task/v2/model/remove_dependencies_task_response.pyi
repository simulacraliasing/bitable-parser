from .remove_dependencies_task_response_body import RemoveDependenciesTaskResponseBody as RemoveDependenciesTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RemoveDependenciesTaskResponse(BaseResponse):
    data: RemoveDependenciesTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
